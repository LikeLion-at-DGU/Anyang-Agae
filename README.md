# 2021 멋쟁이사자처럼 해커톤🦁

## 1. 서비스 소개

### 1.1 서비스 이름

**아프냥 나도아프개(아냥아개)**<br>
[서비스 바로가기 링크](http://52.14.119.174/) <br>
<img src="./anyang_agae/static/img/gallery/logo_green2.png">

### 1.2 주제 및 기획의도

'아프냥 나도아프개'는 동물병원 리뷰 & 반려동물 건강관리 서비스입니다. 현재 우리나라 반려동물 의료체계를 살펴보면, 정확한 진료비를 알 수 없고, 의료사고가 반복되지만 이를 대처할 수 있는 제도가 마련되어 있지 않은 상태이다. 이러럼 의료 체계가 반려동물 친화적이지 않은 상황이기에 사전에 정보를 공유할 수 있는 커뮤니티가 필요한 상황이라고 판단하여 이 서비스를 기획하게 되었다.

### 1.3 팀명 및 팀원

- 팀명 : 아프냥 나도아프개
- [김성민](https://github.com/KimKongDol)
- [안소은](https://github.com/soeun06)
- [이소정](https://github.com/SJLEE316)
- [이소현](https://github.com/LeeSohyun0203)
- [이슬기](https://github.com/Lee-Developer-git)

### 1.4 서비스 소개

## 2. 개발환경

- Framework : Django 3.0.2, Bootstrap 3.4
- Language : Python 3.9.1
- Database : SQLite3
- OS : Window10, MacOS
- IDE : VsCode
- Distribute : aws EC2

## 3. 실행

### 3.1 레포지토리 클론

```
$ git clone https://github.com/LikeLion-at-DGU/Anyang-Agae.git
```

### 3.2 PIP 설치

```
$ pip install -r requirements.txt
```

### 3.3 가상환경 실행

```
$ pipenv shell
```

### 3.4 DB 마이그레이션

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### 3.5 슈퍼유저 생성

```
$ python manage.py createsuperuser
```

### 3.6 서버 실행

```
$ python manage.py runserver
```
