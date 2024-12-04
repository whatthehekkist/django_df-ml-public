     // AJAX로 영화 목록 가져오기
    function loadMovies() {
        $.ajax({
            url: "{% url 'recommend:movies' %}", // Django 뷰로 AJAX 요청
            method: "GET",
            success: function(data) {
               if ($('#movie-list').length) {
                    if ($('#movie-list').hasClass('slick-initialized')) {
                       $('#movie-list').slick('unslick'); // 이미 초기화된 경우 해제
                    }
               }
               $('#movie-list').html(data.movies_html); // AJAX로 가져온 HTML을 삽입
               drawMovies();

            },
            error: function errorHandler() {
                $('#movie-list').html("<p>Error loading recommendations</p>");
            }
        });
    }
    // AJAX로 고객 추천 목록 가져오기
    function loadCustomers() {
         $.ajax({
            url: "{% url 'recommend:customers' model='svd_model' %}", // Django 뷰로 AJAX 요청
            method: "GET",
            success: function(data) {
                if ($('#customer-list').length) {
                    if ($('#customer-list').hasClass('slick-initialized')) {
                       $('#customer-list').slick('unslick'); // 이미 초기화된 경우 해제
                    }
                }
                $('#customer-list').html(data.customers_html); // AJAX로 가져온 HTML을 삽입
                drawCustomers();
            },
            error: function errorHandler() {
                $('#customer-list').html("<p>Error loading recommendations</p>");
            }
        });
    }
    // AJAX로 고객 추천 목록 가져오기
    function loadCustomersNMF() {
        $.ajax({
            url: "{% url 'recommend:customers' model='nmf_model' %}", // Django 뷰로 AJAX 요청
            method: "GET",
            success: function(data) {
                if ($('#customer-list').length) {
                    if ($('#customer-list').hasClass('slick-initialized')) {
                       $('#customer-list').slick('unslick'); // 이미 초기화된 경우 해제
                    }
                }
                $('#customer-list').html(data.customers_html); // AJAX로 가져온 HTML을 삽입
                drawCustomers();
            },
            error: function errorHandler() {
                $('#customer-list').html("<p>Error loading recommendations</p>");
            }
        });
    }

     // AJAX로 고객 추천 목록 가져오기
    function loadCustomersMF() {
        $.ajax({
            url: "{% url 'recommend:customers' model='mf_model' %}", // Django 뷰로 AJAX 요청
            method: "GET",
            success: function(data) {
              if ($('#customer-list').length) {
                    if ($('#customer-list').hasClass('slick-initialized')) {
                       $('#customer-list').slick('unslick'); // 이미 초기화된 경우 해제
                    }
                }
                $('#customer-list').html(data.customers_html); // AJAX로 가져온 HTML을 삽입
                drawCustomers();

            },
          error: function errorHandler() {
                $('#customer-list').html("<p>Error loading recommendations</p>");
            }
        });
    }

    function drawMovies() {
         $('#movie-list').slick({
            draggable : true,
            dots: false,
            infinite: false,
            speed: 500,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            prevArrow: '<button type="button" class="slick-prev">◀</button>',
            nextArrow: '<button type="button" class="slick-next">▶</button>',
            adaptiveHeight: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 3,
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }

    function drawCustomers() {
        $('#customer-list').slick({
                dots: false,
                infinite: false,
                speed: 500,
                slidesToShow: 3,
                slidesToScroll: 1,
                adaptiveHeight: true,
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">◀</button>',
                nextArrow: '<button type="button" class="slick-next">▶</button>',
                responsive: [
                    {
                        breakpoint: 1024,
                        settings: {
                            slidesToShow: 3,
                            slidesToScroll: 3,
                        }
                    },
                    {
                        breakpoint: 600,
                        settings: {
                            slidesToShow: 2,
                            slidesToScroll: 2
                        }
                    },
                    {
                        breakpoint: 480,
                        settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1
                        }
                    }
                ]
            });
    }

    function overlayHandler() {
        // 페이지 로드시 오버레이 표시
        $('.overlay-image').show(); // 필요에 따라 보이게 설정

        // 오버레이를 클릭하면 사라짐
        $('.overlay-image').on('click', function() {
            $(this).hide(); // 클릭 시 오버레이 숨김
        });

        // 닫기 버튼 클릭 시 오버레이 숨김
        $('.close-button').on('click', function() {
            $('.overlay-image').hide(); // 버튼 클릭 시 오버레이 숨김
        });
    }

    // 페이지 로드 시 AJAX로 데이터 로드
    $(document).ready(function() {
        loadMovies();
        loadCustomers();

        overlayHandler();

    });
