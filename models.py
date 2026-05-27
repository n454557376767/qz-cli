from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UserInfo:
    id: int
    username: str
    email: str
    gold: int
    following_count: int
    followers_count: int
    avatar_url: str
    bio: str
    title: str
    title_status: int
    background_url: str
    messages: list = field(default_factory=list)
    experience: int = 0
    level: int = 0
    next_level_exp: int = 0
    is_banned: bool = False
    ban_end_time: Optional[str] = None
    has_checked_in: int = 0
    total_check_ins: int = 0
    consecutive_check_ins: int = 0
    has_unread_notifications: int = 0
    unread_notification_count: int = 0
    total_notification_count: int = 0
    total_likes: int = 0
    has_pending_audit: int = 0

    def display(self):
        import click
        click.echo("用户信息")
        click.echo("━" * 30)
        click.echo(f"ID:           {self.id}")
        click.echo(f"用户名:      {self.username}")
        click.echo(f"邮箱:        {self.email}")
        click.echo(f"等级:        {self.level} (经验: {self.experience}/{self.next_level_exp})")
        click.echo(f"金币:        {self.gold}")
        checked = "已签到" if self.has_checked_in else "未签到"
        click.echo(f"签到:        {checked} (连续{self.consecutive_check_ins}天, 累计{self.total_check_ins}天)")
        click.echo(f"通知:        {self.unread_notification_count}条未读 / 共{self.total_notification_count}条")
        click.echo(f"点赞:        {self.total_likes}")
        click.echo(f"关注:        {self.following_count} | 粉丝: {self.followers_count}")
        click.echo(f"称号:        {self.title}")
        click.echo(f"简介:        {self.bio}")
        banned = f"是 (至 {self.ban_end_time})" if self.is_banned else "否"
        click.echo(f"封禁:        {banned}")
