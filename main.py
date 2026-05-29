import click
import client
from dotenv import dotenv_values, set_key
from dotenv import load_dotenv
import os
import readline
from rich.console import Console

console = Console()
load_dotenv()
qz_post = client.Post(token = os.getenv('token'))
qz_user = client.User(token = os.getenv('token'))

@click.group()
def cli():
    """轻昼cli"""
    pass

@cli.command()
@click.option("-u", "--username", prompt=True, help="用户名")
@click.option("-p", "--password", prompt=True, hide_input=True, help="密码")
def login(username,password):
    """登录"""
    try:
        with console.status("登录中..."):
            token = client.login(username, password).get("token")
    except Exception as e:
        console.print(f"[red]登录失败: {e}[/red]")
        return
    set_key('.env',"token",token)
    console.print("[green]已写入token[/green]")
@cli.group()
def user():
    """用户功能"""
    pass

@user.command()
@click.option("--object", "as_object", is_flag=True, help="返回原始对象")
def profile(as_object):
    """查询自身资料"""
    with console.status("获取资料中..."):
        info = qz_user.get_user_info_by_token()
    if as_object:
        click.echo(info)
    else:
        info.display()

@cli.group()
def post():
    """帖子功能"""
    pass
    
@post.command()
@click.option("-c","--content",help="帖子内容")
@click.option("-t","--title",default=None,help="帖子标题")
@click.option("-m","--is_markdown",is_flag=True,help="是否为markdown")
@click.option("--category_id",help="分区id")
@click.option("--message_type",default=None,help="帖子类型")
@click.option("--debug",default=False,is_flag=True,help="Debug模式")
def send(content, title, is_markdown, category_id, message_type, debug):
    with console.status("发送中..."):
        if is_markdown:
            response = qz_post.send_message(
                content=content,
                title=title,
                message_type=message_type,
                category_id=category_id,
                is_markdown=True
            )
        else:
            response = qz_post.send_message(
                content=content,
                title=title,
                message_type=message_type,
                category_id=category_id
            )
    if debug:
        console.print(f"[dim]API返回：{response}[/dim]")
    console.print("[green]已成功尝试发送[/green]")

@post.command()
@click.option("--category_id", default=1, help="分区ID")
@click.option("--page", default=1, type=int, help="页码")
@click.option("--per_page", default=10, help="每页数量")
@click.option("--message_type", default=None, type=int, help="消息类型(0:文本 1:图片 2:图文 3:帖子 4:Markdown)")
@click.option("--debug", is_flag=True, help="Debug模式")
def get(category_id, page, per_page, message_type, debug):
    """获取消息/帖子"""
    response = qz_post.get_messages(
        category_id=category_id,
        page=page,
        per_page=per_page,
        message_type=message_type
    )
    if debug:
        console.print(f"[dim]API返回：{response}[/dim]")
    if isinstance(response, dict) and response.get("success"):
        for msg in response.get("messages", []):
            msg_type = msg.get("message_type", 0)
            content = msg.get("content", {})
            msg_id = msg.get('message_id')
            username = msg.get('username')

            if msg_type == 3:
                title = content.get("title", "")
                text = content.get("content", "")
                if title:
                    console.print(f"[cyan][{msg_id}][/cyan] [green]{username}[/green]: [yellow][{title}][/yellow] {text}")
                else:
                    console.print(f"[cyan][{msg_id}][/cyan] [green]{username}[/green]: {text}")
            elif msg_type == 1:
                url = content.get('url', '')
                console.print(f"[cyan][{msg_id}][/cyan] [green]{username}[/green]: [magenta][图片][/magenta] {url}")
            else:
                text = content.get('text', '')
                console.print(f"[cyan][{msg_id}][/cyan] [green]{username}[/green]: {text}")

        pagination = response.get("pagination", {})
        console.print(f"--- [bold]第{pagination.get('current_page')}/{pagination.get('total_pages')}页[/bold] 共{pagination.get('total_messages')}条 ---")
    elif isinstance(response, dict):
        console.print(f"[red]获取失败: {response.get('message')}[/red]")
    else:
        console.print(f"[red]获取失败: {response}[/red]")
if __name__ == "__main__":
    cli()