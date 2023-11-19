from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from datetime import date
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  intro = models.TextField()
  body = models.TextField()
  posted_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  body = models.TextField()
  posted_date = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
  #誕生日情報追加
  birth_date = models.DateField(null=True, blank=True)
  # 'groups' フィールドを上書きする必要はありませんが、もし 'related_name' を変更するために定義した場合、このようになります。
  groups = models.ManyToManyField(
      'auth.Group',
      related_name='custom_user_groups',  # ここで 'related_name' をユニークなものに変更
      blank=True,
      help_text='このユーザーが属するグループ。ユーザーは、所属する各グループに付与されたすべての権限を取得します。',
      verbose_name='groups'
  )

  # もし 'user_permissions' フィールドも上書きした場合、同様にユニークな 'related_name' を設定してください。
  user_permissions = models.ManyToManyField(
      'auth.Permission',
      related_name='custom_user_permissions',  # ここでも 'related_name' をユニークなものに
      blank=True,
      help_text='このユーザーに特有の権限。',
      verbose_name='user permissions'
  )
  @property
  def age(self):
    #生年月日が設定されている場合に、年齢を計算して返す
    if self.birth_date:
      today = date.today()
      return today.year - self.birth_date.year - ((today.month, today.day) < self.birth_date.month, self.birth_date.day)
    return None