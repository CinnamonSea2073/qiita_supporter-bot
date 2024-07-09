from tkinter import NO
from typing import Optional
import datetime

class TeamMembership:
    def __init__(self, team_membership: dict) -> None:
        if team_membership is None:
            return None
        self.name: str = team_membership['name']

class User:
    def __init__(self, user: dict) -> None:
        self.id: str = user['id']
        self.name: str = user['name']
        self.description: str = user['description']
        self.facebook_id: str = user['facebook_id']
        self.followees_count: int = user['followees_count']
        self.followers_count: int = user['followers_count']
        self.github_login_name: str = user['github_login_name']
        self.items_count: int = user['items_count']
        self.linkedin_id: str = user['linkedin_id']
        self.location: str = user['location']
        self.organization: str = user['organization']
        self.permanent_id: int = user['permanent_id']
        self.profile_image_url: str = user['profile_image_url']
        self.team_only: bool = user['team_only']
        self.twitter_screen_name: str = user['twitter_screen_name']
        self.website_url: str = user['website_url']

class Tags:
    def __init__(self, tags: list[dict]) -> None:
        self.name: str = tags['name']
        self.versions: list[str] = tags['versions']

class Group:
    def __init__(self, group: dict) -> None:
        if group is None:
            return None
        self.name: str = group['name']
        self.description: str = group['description']
        self.private: bool = group['private']
        self.url_name: str = group['url_name']
        self.updated_at: datetime = datetime.datetime.strptime(group['updated_at'], "%Y-%m-%dT%H:%M:%S%z")
        self.created_at: datetime = datetime.datetime.strptime(group['created_at'], "%Y-%m-%dT%H:%M:%S%z")


class QiitaInfo:
    def __init__(self, qiita_info: dict) -> None:
        self.rendered_body: str = qiita_info['rendered_body']
        self.body: str = qiita_info['body']
        self.coediting: bool = qiita_info['coediting']
        self.comments_count: int = qiita_info['comments_count']
        self.created_at: datetime = datetime.datetime.strptime(qiita_info['created_at'], "%Y-%m-%dT%H:%M:%S%z")
        self.group: Optional[Group] = Group(qiita_info['group'])
        self.id: str = qiita_info['id']
        self.likes_count: int = qiita_info['likes_count']
        self.private: bool = qiita_info['private']
        self.reactions_count: int = qiita_info['reactions_count']
        self.stocks_count: int = qiita_info['stocks_count']
        self.tags: list[Tags] = [Tags(tag) for tag in qiita_info['tags']]
        self.title: str = qiita_info['title']
        self.updated_at: datetime = datetime.datetime.strptime(qiita_info['updated_at'], "%Y-%m-%dT%H:%M:%S%z")
        self.url: str = qiita_info['url']
        self.user: User = User(qiita_info['user'])
        self.page_views_count: int = qiita_info['page_views_count']
        self.team_membership: Optional[TeamMembership] = TeamMembership(qiita_info['team_membership'])
        self.organization_url_name: Optional[str] = qiita_info['organization_url_name']
        self.slide: bool = qiita_info['slide']

    def __str__(self) -> str:
        text = ""
        if self.organization_url_name is not None:
            text += f'**Organization**: {self.organization_url_name}\n'
        text += f'**{self.likes_count}** いいね / **{self.stocks_count}** ストック / **{self.comments_count}** コメント\nタグ: {", ".join([f"`{tag.name}`" for tag in self.tags])}\n'
        return text