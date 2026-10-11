# P’s Pocket 网站栏目

P’s Pocket 的产品介绍、技术支持和隐私政策静态页面，发布在 `meetslink.app`。支持简体中文、香港繁体、台湾繁体和英文。Meets Link 原有内容保留，首页页脚提供 P’s Pocket 入口。

## 页面地址

- 产品页：https://meetslink.app/ps-pocket/
- 技术支持：https://meetslink.app/ps-pocket/support.html
- 隐私政策：https://meetslink.app/ps-pocket/privacy.html

通用入口根据浏览器语言选择页面，用户手动选择优先；指定语言地址保持原语言。偏好仅保存在当前浏览器，不使用 Cookie 或统计。禁用脚本时通用入口仍提供完整英文页面与语言切换链接。

| 语言 | 技术支持 | 隐私政策 |
| --- | --- | --- |
| 简体中文 | https://meetslink.app/ps-pocket/zh-Hans/support.html | https://meetslink.app/ps-pocket/zh-Hans/privacy.html |
| 繁体中文（香港） | https://meetslink.app/ps-pocket/zh-Hant-HK/support.html | https://meetslink.app/ps-pocket/zh-Hant-HK/privacy.html |
| 繁体中文（台湾） | https://meetslink.app/ps-pocket/zh-Hant-TW/support.html | https://meetslink.app/ps-pocket/zh-Hant-TW/privacy.html |
| 英文（美国） | https://meetslink.app/ps-pocket/en-US/support.html | https://meetslink.app/ps-pocket/en-US/privacy.html |

## 维护

- `content.json` 保存四份语言文案。修改后运行 `python3 scripts/build_ps_pocket.py`，一并提交生成的 HTML 和 `sitemap.xml`。
- `assets/site.css` 管理 P’s Pocket 排版；`assets/language.js` 处理通用入口语言选择。无需 npm、第三方字体或 CDN。
- `../meets-link.css` 管理 Meets Link 首页、帮助和隐私政策的排版；栏目生成脚本不编辑这些页面。
- `assets/promo/` 使用原创宣传素材与原创练习宠物画面；`manifest.json` 保存素材散列。栏目不提供商业固件。
- 联系邮箱为现有公开支持地址 `supports@meetslink.app`。调整数据处理方式时，应同步更新四份隐私政策。
- GitHub Pages 从 `main` 分支根目录发布，沿用 `CNAME` 中的 `meetslink.app`。

本地预览：在仓库根目录运行 `python3 -m http.server 18765 --bind 127.0.0.1`，访问 `http://127.0.0.1:18765/ps-pocket/`。资源使用域名根目录路径，应通过 HTTP 预览。

## 公开范围

本仓库只保存可公开的网站源码、文案和宣传素材。提交前应检查新增文件及差异，不要加入 App 闭源源码、签名资料、账号凭据、商业固件、用户存档、设备标识或私人文件。测试截图和内部记录保存在仓库外；忽略规则只能防止部分误提交，不能代替内容检查。
