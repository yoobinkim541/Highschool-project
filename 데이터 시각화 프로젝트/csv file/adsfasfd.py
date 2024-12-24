<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Naver Clone</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .header {
            display: flex;
            align-items: center;
            padding: 10px 20px;
            background-color: #111;
        }
        .header .logo {
            font-size: 24px;
            color: #0acb73;
            margin-right: auto;
        }
        .header .search-bar {
            background-color: #333;
            border: 1px solid #555;
            border-radius: 20px;
            padding: 5px 10px;
            color: #fff;
        }
        .header .search-bar input {
            background: none;
            border: none;
            color: #fff;
            outline: none;
        }
        .header .icons {
            display: flex;
            align-items: center;
        }
        .header .icons img {
            width: 24px;
            height: 24px;
            margin-left: 15px;
        }
        .main {
            display: flex;
            justify-content: space-between;
            padding: 20px;
        }
        .main .news {
            width: 70%;
        }
        .main .sidebar {
            width: 25%;
        }
        .main .news .news-item {
            background-color: #222;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 10px;
        }
        .main .sidebar .ad {
            background-color: #ffcc00;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            color: #000;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: #111;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">N</div>
        <div class="search-bar">
            <input type="text" placeholder="검색어를 입력해 주세요.">
        </div>
        <div class="icons">
            <img src="mail_icon.png" alt="Mail">
            <img src="cafe_icon.png" alt="Cafe">
            <img src="blog_icon.png" alt="Blog">
            <img src="shopping_icon.png" alt="Shopping">
            <img src="news_icon.png" alt="News">
        </div>
    </header>
    <main class="main">
        <div class="news">
            <div class="news-item">뉴스 아이템 1</div>
            <div class="news-item">뉴스 아이템 2</div>
            <div class="news-item">뉴스 아이템 3</div>
        </div>
        <div class="sidebar">
            <div class="ad">광고 배너</div>
            <div class="weather">날씨 정보</div>
        </div>
    </main>
    <footer class="footer">
        네이버 더 안전하고 편리하게 이용하세요
    </footer>
</body>
</html>
