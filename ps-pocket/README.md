# P’s Pocket 网站栏目

独立静态 HTML，不依赖 npm、第三方字体、CDN 或自定义 GitHub Pages 构建流程；一个本站脚本负责语言自动选择和记住手动选择。沿用仓库的 `CNAME`：`meetslink.app`。Meets Link 的现有文字、链接与图片保留；首页、帮助与隐私页通过 `meets-link.css` 调整排版，首页页脚加入 P’s Pocket 入口。

## App Store Connect 地址

发布到现有 Pages 分支并确认 HTTPS 返回 200 后，再填写下列 URL：

| 语言 | 技术支持网址 | 隐私政策网址 |
| --- | --- | --- |
| 简体中文 | https://meetslink.app/ps-pocket/zh-Hans/support.html | https://meetslink.app/ps-pocket/zh-Hans/privacy.html |
| 繁体中文（香港） | https://meetslink.app/ps-pocket/zh-Hant-HK/support.html | https://meetslink.app/ps-pocket/zh-Hant-HK/privacy.html |
| 繁体中文（台湾） | https://meetslink.app/ps-pocket/zh-Hant-TW/support.html | https://meetslink.app/ps-pocket/zh-Hant-TW/privacy.html |
| 英文（美国） | https://meetslink.app/ps-pocket/en-US/support.html | https://meetslink.app/ps-pocket/en-US/privacy.html |

App Store Connect 若只有一个繁体中文栏位，可使用香港或台湾页面；每页都能切换地区语言。全语言通用的入口为：

- 产品页：https://meetslink.app/ps-pocket/
- 隐私政策：https://meetslink.app/ps-pocket/privacy.html
- 技术支持：https://meetslink.app/ps-pocket/support.html

通用地址根据浏览器语言偏好选择对应页面，手动选择的语言优先。指定语言的地址保持原语言，不自动跳转。简体中文对应 zh-Hans；香港／澳门繁体对应 zh-Hant-HK；台湾或其他繁体对应 zh-Hant-TW；英文和无法匹配的语言使用 en-US。跳转保留当前页面类别、查询参数和段落锚点。禁用脚本时通用地址仍展示完整英文页面，语言链接仍可使用。

## 内容与维护

- 维护联系邮箱沿用现有网站公开地址：`supports@meetslink.app`；没有添加表单、营销邮件或自动诊断上传。
- `content.json` 维护四份明确的语言文案。更改后运行 `python3 scripts/build_ps_pocket.py`，并一并提交生成的 HTML 与 `sitemap.xml`。脚本只生成 `ps-pocket/` 中的页面，不编辑原站文件。
- `assets/site.css` 统一页面布局，支持手机、桌面、系统深浅色、键盘焦点与打印。FAQ 使用原生 `<details>`，不开启 JavaScript 也能使用。
- `assets/app-icon.png` 是 App 现有白底原创像素图标的最近邻缩小版。首页复用 App Store 可编辑物料中的原创练习游戏画面，以原生 HTML/CSS 和矢量机身重新排版，展示单机、四机和面对面游玩；不设置独立吉祥物展示框。不包含商业游戏画面、商业固件、固件下载或高还原度外壳图片。
- 地区名称保持为简体 PP吉、香港 PP吱、台湾 PP吉、英文 Pocochi。
- 修改数据处理方式时应同时更新四份隐私政策和更新日期。

## 隐私内容核对边界

页面按 1.0（1.0.5）的实际实现编写：设备私有保存与小组件共享存储；iCloud 可用时默认开启整体自动备份；外部文件夹备份；加密附近通讯；面对面交接在缺少基线时传输原版固件；返回后保留导入固件；Web 搜索使用预设关键词。没有写成“任何数据都不离开设备”，也没有声称固件哈希校验能够确认版权合法性。

依据项目内的 `PrivacyInfo.xcprivacy`、首发功能开关、`PetCloudBackup`、`PetCloudArchive`、`PetBackupService`、`NearbyController`、`PetGameLink` 和固件管理实现核对。没有承诺尚未推出的 Watch 移交、离线成长、持续后台运行、自动画中画或宠物呼叫通知。

官方说明：

- [Apple 审核指南 5.1.1](https://developer.apple.com/app-store/review/guidelines/#privacy)：隐私政策应列明数据处理、用途、保留与删除；网页存在不代表 App 内已接入政策链接。
- [Apple 隐私政策](https://www.apple.com/legal/privacy/en-ww/)
- [Microsoft 隐私声明](https://www.microsoft.com/privacy/privacystatement)
- [GitHub 隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)

## 本地查看

在仓库根目录运行 `python3 -m http.server 18765 --bind 127.0.0.1`，打开 `http://127.0.0.1:18765/ps-pocket/zh-Hans/`。不要直接以 `file://` 打开：资源和导航使用适合域名根目录部署的绝对路径。

这些网页解决隐私政策和技术支持地址的问题。“版权”文本字段仍需在 App Store Connect 填写实际权利人名称（例如 `2026 实际权利人`）；“内容版权”单选声明另行处理，不能用本页或版权年份代替。没有在网页中虚构公司法定名称或第三方授权。

## 本次验证（2026-10-11）

- 15 个 HTML 页面的内部资源、页面链接和段落锚点全部可达；每页保留四种语言切换，未发现重复 ID 或未填占位符。
- 4 种语言 × 3 类页面 × 320/390/1280 像素宽度 × 深/浅色，共 72 项浏览器显示检查通过：HTTP 200、无横向溢出、图片加载成功、选中导航正确。
- FAQ 点击展开、收起及答案可见性通过；三个通用地址在关闭 JavaScript 后仍显示完整页面。
- 浏览器没有加载本站以外的资源，也没有脚本错误。
- 已查看简体首页桌面、隐私页桌面以及支持页手机深浅色截图；布局和对比度正常。
- 重新运行生成脚本后，所有生成 HTML 和 sitemap 的 SHA-256 保持一致。
- 初次建立栏目时，CNAME、contact.json、原 support.html、原 privacy.html 和 global.css 与克隆时逐字节一致。随后按要求调整了 Meets Link 三页排版；CNAME、contact.json、global.css 保持原样。

验证针对本地静态站点，不代表页面已经发布，未修改 App Store Connect 的版权声明或其他表单。

首页调整：已移除五个通用／地区首页中的独立 PP吉展示框及对应未使用图片；文字区改为单栏，已检查实际预览无横向溢出。

隐私页调整：原有完整正文保留（十节，简体正文 25 段）；移除摘要卡片、收紧页头。窄屏目录改为默认折叠，已在 606×774 预览确认第一节正文直接可见、无横向溢出，五个通用／地区政策页的章节与锚点一致。

宣传物料适配（2026-10-11）：`assets/promo/manifest.json` 记录素材来源及散列。八份真实游戏局部和一份原创助手图像逐字节保留，使用的是原创练习固件；未复制商业固件画面。宣传机身沿用原物料的简化矢量轮廓，网页文字可随语言和屏幕宽度自然排版。

首页重排（2026-10-11）：产品首页脱离原来的卡片栅格，使用大字号标题、错落机子、交替布局及暖调深色滤镜展示。支持和隐私页保留阅读布局。新增原始滤镜特写及原创助手挥手姿态，产品展示本身不依赖脚本或外部资源。

最新首页验证：四种语言分别在 1280 与 320 像素宽度检查，无横向溢出或文字溢出；全部八个机子画面加载成功。十五页内部链接、资源、锚点及唯一 ID 通过核对。新背景区的文字对比度均超过 4.5:1，九份 PNG 与原可编辑素材逐字节一致。测试窗口尺寸已恢复，本次未发布。

语言自动选择（2026-10-11）：`assets/language.js` 仅处理本站通用入口与语言链接。唯一浏览器存储键为 `ps-pocket.language`，仅在用户点击语言链接时写入；不使用 Cookie、定位、外部接口或统计。浏览器不允许本地存储时仍可自动选择和手动切换；四份隐私政策同步说明本地语言偏好。

Meets Link 排版调整（2026-10-11）：首页标题和下载入口居中，P’s Pocket 简洁链接放在页脚；帮助页使用联系方式双栏／单栏布局，隐私页限制阅读宽度。三页在 320、390、1280 像素宽度共九项浏览器检查通过，没有横向溢出、图片失败或页脚重叠。原有正文、下载地址、联系方式和图片来源保留。
