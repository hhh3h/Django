Pystagram
=============
> Period: 8~9
***
* functions
 * 사진
  * 사진 올리기
   * 필터 적용
   * 미리보기 이미지(thumbnail image)
   * 사진 자르기, 크기 조절
 * 사진 보기
   * 좋아요 표시 남기기
   * 댓글 남기기, 지우기
  * 사진 삭제
  * 사람 태그 달기
 * 이용자/회원
  * 회원 가입과 탈퇴
  * 로그인, 로그아웃
  * 비밀번호 찾기
  * 프로필 보기
   * 간단한 소개
   * 팔로잉, 팔로워
   * 이용자가 올린 사진
  * 구독하기 (팔로잉(following) 기능)
 * 사진 모아보기
  * 타임라인 : 친구 사진들 보기
  * 인기 사진들 보기
  * 특정 이용자의 사진 보기 => 프로필 보기
 * 그 외
  * 로그아웃 상태에서 접속한 첫 화면
  * 로그인 실패
  * 없는 페이지에 접속했을 때 안내하는 페이지 (일명 404 페이지)
  * 허용하지 않는 페이지에 접속한 경우 처리
   * 기획 정책 상 허용하지 않는 경우
   * 접근 권한이 없는 경우
  * 오류가 발생했을 때 안내하는 페이지
  * 관리자 영역
  * 존재하는 ID나 전자우편 주소인지 검사
* urls
 * 개별 사진 보기 : /photos/<사진 ID="">/
 * 사진에 좋아요 누르기 : /photos/<사진 ID="">/like/
 * 사진에 댓글 달기 : /photos/<사진 ID="">/comment/
  * 사진에 달린 댓글 가져오기 : /photos/<사진 ID="">/get_comments/
  * 사진에 달린 댓글 지우기 : /photos/<사진 ID="">/comment/<댓글 ID="">/delete/
 * 사진에 태그 달기 : /photos/<사진 ID="">/tag/
 * 인기 사진 : /popular/
 * 이용자 개별 타임라인 : /timeline/
 * 특정 이용자가 올린 사진 : /users/<이용자 ID="">/
 * /photos/<사진 ID="">/delete/
 * 회원 가입 URL은 /accounts/registration/ 
 * 로그인 : /accounts/login/
 * 로그아웃 : /accounts/logout/
 * 프로필 : /users/<이용자 ID="">/
 * 이용자가 구독하는 팔로잉 페이지는 /users/<이용자 ID="">/following/
 * 이용자를 구독하는 팔로워 페이지는 /users/<이용자 ID="">/followers/
 * 구독하기 : /users/<이용자 ID="">/follow/ 

![Alt text](http://blog.hannal.com/assets/uploads/2014/08/01-Scene_flow.png)

***
* [hannal](Link: http://blog.hannal.com/category/start-with-django-webframework/)

