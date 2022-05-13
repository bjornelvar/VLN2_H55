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


    // ENTER TO SEARCH FUNCTIONS
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

    // SOLD FILTER IN MY LISTINGS FUNCTIOn
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
        let input = document.getElementById('staticEmail')
        document.getElementById('unlock_typing').classList.replace('edit_email-btn', 'visually-hidden')
        document.getElementById('change_email').removeAttribute('disabled')
        input.classList.replace('form-control-plaintext', 'form-control')
        input.removeAttribute('readonly')

    }) // end of unlock typing function

    // PRESERVE ORDER BY PARAMETER ON PAGE RELOAD FUNCTION

    $('#send_email').on('click', function (){
        let text_element = document.createElement('p');
        let text = document.createTextNode("An email has been sent to you, if you didn't recieve an email click the link again.");
        text_element.appendChild(text);
        let div = document.getElementById('verify_link');
        div.appendChild(text_element);


    });

    $(".page-link").on( 'click', function (element) {
    // $(element).attr('href', function() {
        let href = $(this).attr('href')
        let params = new URLSearchParams(window.location.search);
        let order_by_string = params.get('order_by');
        if (order_by_string != null) {
            $(this).attr("href", href + "&order_by=" + order_by_string)
        }

    });


 });




