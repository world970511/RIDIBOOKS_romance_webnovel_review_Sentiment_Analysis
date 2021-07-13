# RIDIBOOKS_romance_webnovel_review_Sentiment_Analysis<br>(리디북스 로맨스 웹소설 리뷰 감성분류)
<p>
<h1>crawler_code</h1>

*RIDI_crawler_code : 리디북스 북 코드를 찾는 코드

*RIDI_crawler_review: 리디북스 리뷰를 긁는 코드
</p>

<p>
  <h1>data</h1>
  <h3>1.ridi_code.txt</h3>
  키워드[단행본]를 쳐서 리뷰 많은 순으로 긁어온 북코드.<br>
  약 2000개의 북코드가 들어 있습니다.<br>
  <h3>2.origin_all_data.txt</h3>

  언어: 한국어<br>
  출처: 리디북스(https://ridibooks.com/romance/)<br>
  수집 기간: ~2020.05.23<br>
  - 리디북스 로맨스에서 후기를 별점과 함께 수집했습니다.<br> 첫번째 필드에는 별점(1 ~ 5), 두번째 필드에는 텍스트가 위치합니다. <br>긍/부정으로 분류하기 애매한 3점에 해당하는 텍스트   는 0, <br>긍정(4 ~ 5점)은 1<br> 부정(1 ~ 2점) 은-1 로 나타내었습니다. <br>또한 내용과 관련 없는 이벤트 관련 글은 최대한 삭제했습니다.<br><br>
  총계:579,867<br>
  부정:55434<br>
  불명확:76379<br>
  긍정:445054<br>

  <h3>3.result_all_data.txt</h3>

  언어: 한국어<br>
  출처: 리디북스(https://ridibooks.com/romance/)<br>
  수집 기간: ~2020.05.23<br>
  - 리디북스 로맨스에서 후기를 별점과 함께 수집한 것을 바탕으로 긍정/부정인 데이터 개수를 동일하게 만든 데이터입니다.<br> 첫번째 필드에는 별점(1 ~ 5), 두번째 필드에는 텍스트가 위치   합니다.<br>긍정(4 ~ 5점)은 1<br> 부정(1 ~ 2점) 은-1 로 나타내었습니다. <br>또한 내용과 관련 없는 이벤트 관련 글은 최대한 삭제했습니다.<br><br>
  총계:110,868<br>
  부정:55434<br>
  긍정:55434<br>
  
  <h3>4.result_title_info_data.txt</h3>
  언어: 한국어<br>
  출처: 리디북스(https://ridibooks.com/romance/)<br>
  수집 기간: ~2020.06.07<br>
   - 리디북스 로맨스에서 제목/아이디/후기/별점을 수집한 것을 바탕으로 긍정/부정인 데이터 개수를 동일하게 만든 데이터입니다.
   <br>총 100권의 책에 관련된 데이터가 존재합니다.<br> 첫번째  필드에는 책 제목<br> 두번째 필드에는 리뷰 작성 아이디
   <br>세번째 필드는 별점(1 ~ 5)<br>마지막 필드에는 텍스트가 위치합니다.
   <br>긍정(4 ~ 5점)은 1<br> 부정(1 ~ 2점) 은-1 로 나타내었습니다. <br>또한 내용과 관련 없는 이벤트 관련 글은 최대한 삭제했습니다.<br><br>
  </p>
  
  <h3>5.all_result_title_with_info_data.txt</h3>
  언어: 한국어<br>
  출처: 리디북스(https://ridibooks.com/romance/)<br>
  수집 기간: ~2020.07.10<br>
   - 리디북스 로맨스에서 제목/키워드/전체평점/평가인원을 기준으로 수집한 데이터입니다.
   <br>총 5731권의 책에 관련된 데이터가 존재합니다.<br> 첫번째  필드에는 책 제목<br> 두번째 필드에는 키워드<br> 세번째는 평점
   <br>마지막 필드에는 평가 인원수가 위치합니다.
   <br>또한 책 제목을 기준으로 중복되는 것과 누락된 내용은 모두 삭제했습니다.<br><br>
  </p>


<p>
  <h1>anlay_ridi.ipynb</h1>
  - 구글 코랩으로 작성한 데이터 전처리/감성 분류 코드<br>
  데이터는 위의 자료(result_all_data.txt)를 사용했고
  <br>https://wikidocs.net/44249 와 도서 <파이썬 머신러닝 완벽 가이드> 를  참조하여 작성하였습니다.
  <br>테스트 정확도:  0.9164

</p>



