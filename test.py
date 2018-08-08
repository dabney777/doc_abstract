#!/usr/bin/python
# -*- coding: utf-8 -*-

from textteaser import TextTeaser

# article source: https://blogs.dropbox.com/developers/2015/03/limitations-of-the-get-method-in-http/
# title = "Limitations of the GET method in HTTP"
# text = "We spend a lot of time thinking about web API design, and we learn a lot from other APIs and discussion with their authors. In the hopes that it helps others, we want to share some thoughts of our own. In this post, we’ll discuss the limitations of the HTTP GET method and what we decided to do about it in our own API.  As a rule, HTTP GET requests should not modify server state. This rule is useful because it lets intermediaries infer something about the request just by looking at the HTTP method.  For example, a browser doesn’t know exactly what a particular HTML form does, but if the form is submitted via HTTP GET, the browser knows it’s safe to automatically retry the submission if there’s a network error. For forms that use HTTP POST, it may not be safe to retry so the browser asks the user for confirmation first.  HTTP-based APIs take advantage of this by using GET for API calls that don’t modify server state. So if an app makes an API call using GET and the network request fails, the app’s HTTP client library might decide to retry the request. The library doesn’t need to understand the specifics of the API call.  The Dropbox API tries to use GET for calls that don’t modify server state, but unfortunately this isn’t always possible. GET requests don’t have a request body, so all parameters must appear in the URL or in a header. While the HTTP standard doesn’t define a limit for how long URLs or headers can be, most HTTP clients and servers have a practical limit somewhere between 2 kB and 8 kB.  This is rarely a problem, but we ran up against this constraint when creating the /delta API call. Though it doesn’t modify server state, its parameters are sometimes too long to fit in the URL or an HTTP header. The problem is that, in HTTP, the property of modifying server state is coupled with the property of having a request body.  We could have somehow contorted /delta to mesh better with the HTTP worldview, but there are other things to consider when designing an API, like performance, simplicity, and developer ergonomics. In the end, we decided the benefits of making /delta more HTTP-like weren’t worth the costs and just switched it to HTTP POST.  HTTP was developed for a specific hierarchical document storage and retrieval use case, so it’s no surprise that it doesn’t fit every API perfectly. Maybe we shouldn’t let HTTP’s restrictions influence our API design too much.  For example, independent of HTTP, we can have each API function define whether it modifies server state. Then, our server can accept GET requests for API functions that don’t modify server state and don’t have large parameters, but still accept POST requests to handle the general case. This way, we’re opportunistically taking advantage of HTTP without tying ourselves to it."

# article source: http://www.xinhuanet.com/world/2018-08/07/c_129928410.htm
title = "新闻分析：土美关系急转直下能否峰回路转"
text='''近期，作为北约盟友的美国和土耳其相互制裁，近乎撕破脸的架势。有报道称，土耳其将派出代表团赴华盛顿就双边关系紧张局势进行沟通。
　　分析人士指出，土美关系不断恶化的现实，暴露了两个重要的北约盟友在一系列国际和地区事务上的深刻分歧，双方持续对抗将加剧北约内部分化，让业已混乱的中东局势更加复杂。
　　争议焦点
　　７月举行北约峰会上，土耳其总统埃尔多安和美国总统特朗普实现会面，此后双边关系有所回暖。美土关系再度急转直下的一个争议焦点，是美籍牧师布伦森案。
　　土耳其２０１６年７月发生未遂军事政变。政变平息后，土耳其方面逮捕布伦森，指控他从事反政府间谍活动。美方就释放布伦森一事与土耳其方面多次交涉。北约峰会特朗普同埃尔多安会面之后，外界原本对此案有所期待，没承想口水仗不断升级,甚至演变为相互制裁。
　　美国财政部８月１日宣布对土内政部长与司法部长实行制裁。这是美国政府首次对北约成员国实施经济制裁，实属罕见。埃尔多安政府之后随即宣布对等报复措施，冻结美司法部长和内政部长在土资产。对此，美国助理国家安全顾问朱莉安·史密斯说，这意味着“美土关系已经处于危机之中”。
　　四重矛盾
　　实际上，此轮争端只是２０１６年以来土美关系持续走低的一个缩影。自土耳其发生未遂军事政变后，土美关系进入新的波动周期，双方在核心利益上的分歧越来越深，突出表现在四个方面。
　　首先，引渡宗教人士居伦问题。土政府认为，侨居美国的宗教人士居伦是２０１６年政变的幕后主谋，并将其领导的“居伦运动”列为恐怖组织。土方多次要求将其引渡回国接受调查，但美国至今没有同意。此外，围绕“居伦运动”的调查中，有数十名土美双重国籍公民被捕。
　　其二，叙利亚库尔德武装的合法性问题。库尔德武装问题始终是土耳其关于领土安全的重大关切，土耳其军队在土东南部和叙利亚、伊拉克境内多次打击库尔德人武装，而美国却在叙利亚战场扶持“叙利亚民主军”等库尔德武装，引发土耳其担忧。这一问题也暴露出土美在叙利亚战场的利益分歧。
　　第三，军购问题。土耳其的常备军数量位居北约第二。近期，土耳其欲购买俄罗斯Ｓ－４００防空导弹系统一事持续发酵，引发美国和其他北约盟友担忧。美国威胁向土停售Ｆ－３５战机，土方则威胁收回美空军基地。美国最新通过的“２０１９财年国防授权法案”中还要求暂停向土耳其交付Ｆ－３５战机。
　　第四，制裁伊朗问题。美国宣布于７日对伊朗部分非能源领域重启制裁。土方此前表示，不会响应美国的制裁要求。数据显示，今年前４个月土耳其从伊朗进口原油超过３００万吨，占土耳其全部原油进口的５５％。分析人士认为，土耳其作为缺油国，对伊朗石油和天然气供应有依赖，短期内不会加入对伊朗的制裁。
　　渐行渐远
　　土耳其是北约中唯一的中东国家，美国需要土耳其在中东地区发挥作用，更不愿看到土耳其倒向俄罗斯。美国国务卿蓬佩奥最近在东南亚访问时仍不忘强调，“土耳其是北约盟友，美国非常愿意和它继续开展合作”。
　　然而，土耳其对自身的定位是地区大国，在外交和安全防务上有着很强的自主意识，特别是近年来其在地区事务中发挥更大影响力的意愿不断增强，这使得它与美国等传统西方盟友间在战略方向上的矛盾日益凸显。
　　美国国务院前中东事务高级官员韦恩·怀特指出，美国和土耳其已经有太多矛盾，两国早已渐行渐远，布伦森案不过是最新导火索。尤其是美国在叙利亚支持库尔德武装的做法可能让土耳其和俄罗斯、伊朗进一步走近，这将让土耳其和西方的裂痕进一步拉大。
　　在美国智库布鲁金斯学会高级研究员达雷尔·韦斯特看来，总体而言，土耳其将在对外政策上更加疏远美国，这将让美国的中东政策面临更多未来挑战。
　　不过，美国华盛顿近东政策研究所资深研究员戴维·波洛克认为，美土关系虽面临很多问题，但鉴于美国仍表明愿就分歧同土耳其继续对话，这说明双方并不想立即撕破脸，依旧可能在包括叙利亚库尔德问题、美对土耳其军售等问题上寻求妥协并合作。'''

tt = TextTeaser()

sentences = tt.summarize(title, text)

for sentence in sentences:
    print(sentence)