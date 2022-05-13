$(document).ready(function() {

    // NAVBAR SEARCH FUNCTION
    $("#search_term").on("input", function () {
        console.log("test")
        $("#search_button").attr("href", "/items/search/?search_val=" + $("#search_term").val().replace(/ /g, "+"))
    });
    $("#search_button").on("click", function () {
        if ($("#category-select").val() != "") {
            $("#search_button").attr("href", "/items/search/?search_val=" + $("#search_term").val().replace(/ /g, "+") + "&category=" + $("#category-select").val())
        }
    });

    // HOME SEARCH BAR FUNCTION
    $("#search_term_home").on("input", function () {
        console.log("test")
        $("#search_button_home").attr("href", "/items/search/?search_val=" + $("#search_term_home").val().replace(/ /g, "+"))
    });
    $("#search_button_home").on("click", function () {
        if ($("#category-select_home").val() != "") {
            $("#search_button_home").attr("href", "/items/search/?search_val=" + $("#search_term_home").val().replace(/ /g, "+") + "&category=" + $("#category-select_home").val())
        }
    });

    $("#search_term").keypress(function (e) {
        if (e.which == 13) {
            $("#search_button").get(0).click();
            }
    });

    $("#search_term_home").keypress(function (e) {
        if (e.which == 13) {
            $("#search_button_home").get(0).click();

            }
    });


    // ORDER BY FUNCTION
    $('#order_by_menu li a').on('click', function(){
        let txt = ($(this).data('value'));
        let pathname = String(window.location.pathname);

        if (pathname.includes("/items/search/")) {
            let searchParams = new URLSearchParams(window.location.search);
            let category_string = searchParams.get('category');
            let search_string = searchParams.get('search_val');
            pathname = (pathname + "?search_val=" + String(search_string));
                if (category_string != null) {
                    pathname = pathname + "&category=" + String(category_string);
                }
            $(this).attr("href", pathname + "&order_by=" + txt)
                }

        else {
            $(this).attr("href", "?order_by=" + txt)
        }
    });


    $("#sold-filter").on("click", function () {
    let pathname = String(window.location.pathname);
    let params = new URLSearchParams(window.location.search);
    let pageString = params.get('page');
    if (pageString == null) {
        pageString = 1;
    }
    if($('#sold-filter').prop('checked')) {
        window.location.replace(pathname + '?page=' + pageString);
    }
    else {
        window.location.replace(pathname + '?page=' + pageString + "&sold=false");
    }

    });


    $('#slider-left').on('click', function (){
        document.getElementById('scrollable_container').scrollLeft -= 400;
    });
    $('#slider-right').on('click', function (){
        document.getElementById('scrollable_container').scrollLeft += 400;
    });


    $('#unlock_typing').on('click', function (){
        input = document.getElementById('staticEmail')
        document.getElementById('unlock_typing').classList.replace('edit_email-btn', 'visually-hidden')
        document.getElementById('change_email').removeAttribute('disabled')
        input.classList.replace('form-control-plaintext', 'form-control')
        input.removeAttribute('readonly')

    })
});







    // $("#order_val").on("mouseover", function () {
    //     console.log("Hello", $("#order_val").attr("data-value"))
    //     $("#order_val").attr("href", "?order_by=" + $("#order_val").attr("data-value"))
    // });
    // $("#order_val1").on("mouseover", function () {
    //     console.log("Hello", $("#order_val1").attr("data-value"))
    //     $("#order_val1").attr("href", "?order_by=" + $("#order_val1").attr("data-value"))
    // });
    // $("#order_val2").on("mouseover", function () {
    //     console.log("Hello", $("#order_val2").attr("data-value"))
    //     $("#order_val2").attr("href", "?order_by=" + $("#order_val2").attr("data-value"))
    // });
    // $("#order_val3").on("mouseover", function () {
    //     console.log("Hello", $("#order_val3").attr("data-value"))
    //     $("#order_val3").attr("href", "?order_by=" + $("#order_val3").attr("data-value"))
    // });

