{% extends 'base.html' %}
{% load static %}
{% block title %} 지역별 통계정보 {% endblock %}
{% block content %}

<main id="main" class="main">

    <div class="pagetitle">
        <h1>지역별 통계정보</h1>
        <nav>
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                <li class="breadcrumb-item">Stat</li>
                <li class="breadcrumb-item active">Region</li>
            </ol>
        </nav>
    </div><!-- End Page Title -->

    <div id="region">
        <button type="button" value="11" onclick="">서울</button>
        <button type="button" value="21" onclick="">부산</button>
        <button type="button" value="22" onclick="">대구</button>
        <button type="button" value="23" onclick="">인천</button>
        <button type="button" value="24" onclick="">광주</button>
        <button type="button" value="25" onclick="">대전</button>
        <button type="button" value="26" onclick="">울산</button>
        <button type="button" value="29" onclick="">세종</button>
        <button type="button" value="31" onclick="">경기</button>
        <button type="button" value="32" onclick="">강원</button>
        <button type="button" value="33" onclick="">충북</button>
        <button type="button" value="34" onclick="">충남</button>
        <button type="button" value="35" onclick="">전북</button>
        <button type="button" value="36" onclick="">전남</button>
        <button type="button" value="37" onclick="">경북</button>
        <button type="button" value="38" onclick="">경남</button>
        <button type="button" value="39" onclick="">제주</button>
    </div>
    <section class="section">
        <div class="row">
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">임금현황 - 금액별 평균</h5>
                        <!-- Bar Chart - 임금현황 금액  -->
                        <div id="barChart"></div>
                        <script>
                            let pay_avg_list = {{ pay_avg_list }}
                            document.addEventListener("DOMContentLoaded", () => {
                                chart1 = new ApexCharts(document.querySelector("#barChart"), {
                                    series: [{
                                        data: pay_avg_list
                                    }],
                                    chart: {
                                        type: 'bar',
                                        height: 350,
                                    },
                                    plotOptions: {
                                        bar: {
                                            borderRadius: 4,
                                            horizontal: true,
                                        }
                                    },
                                    dataLabels: {
                                        enabled: false
                                    },
                                    xaxis: {
                                        categories: ['시급', '월급', '연봉'
                                        ],
                                    }
                                })
                                chart1.render();
                            });
                        </script>
                        <!-- End Bar Chart -->
                    </div>
                </div>
            </div>



            <div class="col-lg-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">임금 현황 - 종류</h5>

                        <!-- Donut Chart - 지역별(직종별) 임금 현황 -->
                        <div id="donutChart"></div>

                        <script>
                            let paytype_list = {{ paytype_list }}

                            document.addEventListener("DOMContentLoaded", () => {
                                chart2 = new ApexCharts(document.querySelector("#donutChart"), {
                                    // series: [3, 19, 45, 49],
                                    series: paytype_list,
                                    chart: {
                                        height: 350,
                                        type: 'donut',
                                        toolbar: {
                                            show: true
                                        }
                                    },
                                    labels: ['시급', '월급', '연봉'],
                                })
                                chart2.render();
                            });
                        </script>
                        <!-- End Donut Chart -->
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">직종 현황</h5>

                        <!-- Pie Chart - 지역별 직종 현황-->
                        <div id="pieChart"></div>

                        <script>

                            let worktype_list = {{ worktype_list }}
                            document.addEventListener("DOMContentLoaded", () => {
                                chart3 = new ApexCharts(document.querySelector("#pieChart"), {
                                    series: worktype_list,
                                    chart: {
                                        height: 350,
                                        type: 'pie',
                                        toolbar: {
                                            show: true
                                        }
                                    },

                                    // labels: ['경영·사무·금융·보험', '연구 및 공학기술', '교육·법률·사회복지', '보건·의료', '예술·디자인·방송·스포츠', '미용·여행·숙박·음식·경비', '영업·판매·운전·운송', '건설·채굴', '설치·정비·생산-기계', '설치·정비·생산-전기', '설치·정비·생산-화학', '설치·정비·생산-인쇄·목재', '농림어업직']
                                    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                                })
                                chart3.render();
                            });
                        </script>
                        <!-- End Pie Chart -->

                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">워드클라우드</h5>

                        <div id="wordcloud"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- test -->
    <script>
        const donutchart = document.querySelector("#wordcloud")
        // console.log(donutchart)


        var tmptmp = [1, 2, 3, 4, 5]
        document.addEventListener("DOMContentLoaded", () => {
            new ApexCharts(document.querySelector("#wordcloud"), {
                series: tmptmp,
                chart: {
                    id: 'mychart',
                    height: 350,
                    type: 'pie',
                    toolbar: {
                        show: true
                    }
                },
                labels: [1, 2, 3, 4, 5,]
            }).render()

        });


    </script>



</main><!-- End #main -->
{% endblock %}

{% block script %}
<script src="{% static 'showstat/showstat.js' %}"></script>
{% endblock %}