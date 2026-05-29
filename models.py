from dataclasses import dataclass, field
from typing import Optional
from rich.table import Table
from rich.console import Console


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
        console = Console()
        table = Table(show_header=False, box=None, highlight=True)
        table.add_column("key", style="bold yellow")
        table.add_column("value", style="cyan")

        table.add_row("ID", str(self.id))
        table.add_row("用户名", self.username)
        table.add_row("邮箱", self.email)
        table.add_row("等级", f"{self.level} (经验: {self.experience}/{self.next_level_exp})")
        table.add_row("金币", str(self.gold))
        checked = "已签到" if self.has_checked_in else "未签到"
        table.add_row("签到", f"{checked} (连续{self.consecutive_check_ins}天, 累计{self.total_check_ins}天)")
        table.add_row("通知", f"{self.unread_notification_count}条未读 / 共{self.total_notification_count}条")
        table.add_row("点赞", str(self.total_likes))
        table.add_row("关注/粉丝", f"{self.following_count} / {self.followers_count}")
        table.add_row("称号", self.title)
        table.add_row("简介", self.bio)
        banned = f"是 (至 {self.ban_end_time})" if self.is_banned else "否"
        table.add_row("封禁", banned)

        console.print(table)
