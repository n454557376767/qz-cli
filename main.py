import click
import client
from dotenv import dotenv_values, set_key

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
    
if __name__ == "__main__":
    cli()