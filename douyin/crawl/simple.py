import requests
url = "https://www.douyin.com/search/{}?aid=9d40feab-4eb2-4977-86f7-ab523d593d65&publish_time=0&sort_type=0&source=search_sug&type=video"
header = {
    'cookie':'ttwid=1|-dhz2UracNIdJyG6_zRTnpNUw6Kg1ncSNPXdWOMhgPU|1625491042|167cd47010a6d2c5b22a44f4d8456a0461196e9109403b55cd07c1cef74f1b0e; douyin.com; passport_csrf_token_default=d69e94b9396497fd42e351767fa5bd20; passport_csrf_token=d69e94b9396497fd42e351767fa5bd20; s_v_web_id=verify_5fa4ca0e3772b51cff567cb0f9f33603; odin_tt=3832d7cca0ea967017be71b24ae21e558918af2e6c31a47e2c76d4c70f3cc6d64637fe44ff77fc59f2dafcb5e4a49df97ff41d832bfb73d296436fbbb292a5ed; n_mh=oFv76n1pHhYkXAo-h9ayj9iKM_Bb-I8-vvQkxtAR7Iw; sso_auth_status=c29098be6eb404bfc3871ea11e4095f1; sso_auth_status_ss=c29098be6eb404bfc3871ea11e4095f1; sso_uid_tt=c4b01997dbe67cbffd6fae48ae7c0277; sso_uid_tt_ss=c4b01997dbe67cbffd6fae48ae7c0277; toutiao_sso_user=2d8af61d4830fa68255899c5b30069a0; toutiao_sso_user_ss=2d8af61d4830fa68255899c5b30069a0; d_ticket=fd086ae93a6f62d0acbc687efff641aacbbe7; passport_auth_status_ss=802a26ae216f48ef9565edc41be550ca,825f7b260362f86ee02e33dede48a376; sid_guard=55652b53106ea371b74200587446e742|1625491414|5184000|Fri,+03-Sep-2021+13:23:34+GMT; uid_tt=0b446f36b17fd8c7e6aec7bac65a1fa3; uid_tt_ss=0b446f36b17fd8c7e6aec7bac65a1fa3; sid_tt=55652b53106ea371b74200587446e742; sessionid=55652b53106ea371b74200587446e742; sessionid_ss=55652b53106ea371b74200587446e742; passport_auth_status=802a26ae216f48ef9565edc41be550ca,825f7b260362f86ee02e33dede48a376; MONITOR_WEB_ID=b1ba0910-1c73-4898-b526-d8b1825780a5',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    '_signature':'_02B4Z6wo00901uWHVLwAAIDBVXa4ddrXa6Llh1AAANmSc5'
}
url = 'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=0&keyword=%E5%AE%A0%E7%89%A9%E7%8C%AB&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=30&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.124+Safari%2F537.36&browser_online=true&_signature=_02B4Z6wo00901uWHVLwAAIDBVXa4ddrXa6Llh1AAANmSc5'

req = requests.get(url, headers=header)
print(req.text)
with open("1.html",'w') as f:
    f.write(req.text)