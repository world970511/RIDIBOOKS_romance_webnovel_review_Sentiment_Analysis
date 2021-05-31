# RIDIBOOKS_romance_webnovel_review_Sentiment_Analysis<br>(리디북스 로맨스 웹소설 리뷰 감성분류)
<p>
<h1>crawler_code</h1>

*RIDI_crawler_code : 리디북스 북 코드를 찾는 코드

*RIDI_crawler_review: 리디북스 리뷰를 긁는 코드

*ridi_code.txt :키워드[연재중/연재완료/단행본]를 쳐서 리뷰 많은 순으로 긁어온 북코드. 약 6700개
</p>

<p>
  <h1>data</h1>
  
  <h3>1.origin_all_data.txta</h3>

언어: 한국어<br>
출처: 리디북스(https://ridibooks.com/romance/)<br>
수집 기간: ~2020.05.23<br>
- 리디북스 로맨스에서 후기를 별점과 함께 수집했습니다.<br> 첫번째 필드에는 별점(1 ~ 5), 두번째 필드에는 텍스트가 위치합니다. <br>긍/부정으로 분류하기 애매한 3점에 해당하는 텍스트는 0, <br>긍정(4 ~ 5점)은 1<br> 부정(1 ~ 2점) 은-1 로 나타내었습니다. <br>또한 내용과 관련 없는 이벤트 관련 글은 최대한 삭제했습니다.<br><br>

<h3>2.result_all_data</h3>

언어: 한국어<br>
출처: 리디북스(https://ridibooks.com/romance/)<br>
수집 기간: ~2020.05.23<br>
- 리디북스 로맨스에서 후기를 별점과 함께 수집한 것을 바탕으로 긍정/부정인 데이터 개수를 동일하게 만든 데이터입니다.<br> 첫번째 필드에는 별점(1 ~ 5), 두번째 필드에는 텍스트가 위치합니다.<br>긍정(4 ~ 5점)은 1<br> 부정(1 ~ 2점) 은-1 로 나타내었습니다. <br>또한 내용과 관련 없는 이벤트 관련 글은 최대한 삭제했습니다.<br><br>
총: 97566<br>
부정:48783 <br>
긍정:48783 <br>
</p>

<p>
<h1>anlay_ridi.ipynb</h1>
- 구글 코랩으로 작성한 데이터 전처리/감성 분류 코드<br>데이터는 위의 자료(result_all_data.txt)를 사용했고<br>https://wikidocs.net/44249 와 도서 <파이썬 머신러닝 완벽 가이드> 를 참조하여 작성하였습니다.<br>테스트 정확도: 0.9089

</p>



