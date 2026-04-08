import click
import client
from dotenv import dotenv_values, set_key
from dotenv import load_dotenv
import os
import readline
load_dotenv()
qz_post = client.Post(token = os.getenv('token'))

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
        token = client.login(username, password).get("token")
    except Exception as e:
        click.echo(f"登录失败: {e}", err=True)
        return
    set_key('.env',"token",token)
    click.echo("已写入token")
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
def send_post(content, title, is_markdown, category_id, message_type, debug):
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
        click.echo(f"API返回：{response}")
    click.echo(f"已成功尝试发送")
if __name__ == "__main__":
    cli()