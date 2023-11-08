# project_Blog
- Django로 블로그를 제작하는 프로젝트

## 1. 목표와 기능

### 1.1 목표
- Django로 블로그 만들기
- 개발에 관련된 내용을 주로 기록하고 공유
- 일상 생활의 다른 주제의 내용도 다른 카테고리로 게시하고 공유

### 1.2 기능
- 기록한 내용을 언제든지 다시 검색하여 볼 수 있음.
- 여러 내용을 공유하며 여러 사람의 의견들을 공유 가능.


## 2. 개발환경
- Django
- python
- html


## 3. 프로젝트 구조와 개발 일정

### 3-1. 디렉토리 구조
![디렉토리구조](https://github.com/hoyonzz/project_Blog/assets/129498722/d1457b1a-1858-4d9d-9e9f-1958812a9074)

### 3-2. WBS
![image](https://github.com/hoyonzz/project_Blog/assets/129498722/63ddfe1c-2697-4355-b40d-c11b99fb6c23)


## 4. URL 구조
![image](https://github.com/hoyonzz/project_Blog/assets/129498722/3fa6ccf5-69bb-4bfe-8567-fcda1901b977)

## 5. ERD
![Uploading 281244606-f53399cb-0099-4f29-9675-c0f251feadb3.png…]()


## 6. 주요 기능
#### 1) 메인페이지
![index](https://github.com/hoyonzz/project_Blog/assets/129498722/352d02cf-5c95-480b-92e9-48f8b2313d25)
- 프로젝트 소개와 블로그 제목, 입장하기 버튼을 구현

#### 2) blog메인페이지
![blog](https://github.com/hoyonzz/project_Blog/assets/129498722/d8356a16-4b80-4433-b9f6-635b23f2d127)
- 검색 기능과 로그인, 회원가입, 계정 프로필, 카테고리들을 구현

#### 2_1) blog메인_로그인 후
![로그인5](https://github.com/hoyonzz/project_Blog/assets/129498722/00a0f3cb-2ea6-4fa5-b5a3-11770e285b02)
- 로그인을 하게 되면 로그인 버튼이 글쓰기 버튼으로 바뀌게 되고, 프로필에 계정 정보를 표시

#### 3) 게시글 상세 페이지
![게시글상세페이지](https://github.com/hoyonzz/project_Blog/assets/129498722/37e52111-5984-4afd-a0c4-f303c8b34908)
- 게시글의 제목, 작성자, 작성일, 카테고리, 내용, 편집, 삭제 뒤로돌아가기 버튼을 구현

#### 4) 글 작성
![게시글작성](https://github.com/hoyonzz/project_Blog/assets/129498722/c2bd56e2-4cd3-4103-b5d9-5992a3498287)
- 카테고리, 글제목, 글 내용, 파일첨부

#### 5) 게시글 편집
![게시물편집](https://github.com/hoyonzz/project_Blog/assets/129498722/92f47dbd-82a6-4946-adf1-604a57adb63c)
- 글 제목, 내용, 이미지, 첨부파일, 카테고리, 태그를 수정하는 폼을 구현

#### 6) 회원가입
![회원가입](https://github.com/hoyonzz/project_Blog/assets/129498722/f6577201-c6ac-407a-8115-95a70540346d)
- 이름, 이메일, 비밀번호를 입력하여 회원가입

#### 7) 로그인
![로그인](https://github.com/hoyonzz/project_Blog/assets/129498722/9b16e136-4223-45f7-8caa-828f159ca43b)
- 로그인 버튼으로 로그인 창으로 이동, 이메일과 비밀번호를 입력하고 로그인하면 블로그 리스트 화면으로 이동하게 되고, 로그인 후에는 글작성 가능할 수 있도록 로그인버튼이 write 버튼으로 변경됨.
