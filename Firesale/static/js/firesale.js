$(document).ready(function() {
    $("#search_term").on("input", function () {
        console.log("test")
        $("#search_button").attr("href", "/items/search/?search_val=" + $("#search_term").val().replace(/ /g, "%20"))
    });
    $("#search_button").on("click", function () {
        if ($("#category-select").val() != "") {
            $("#search_button").attr("href", "/items/search/?search_val=" + $("#search_term").val().replace(/ /g, "%20") + "&category=" + $("#category-select").val())
        }
    });
    $("#order_val").on("mouseover", function () {
        console.log("Hello", $("#order_val").attr("data-value"))
        $("#order_val").attr("href", "/items/?order_by=" + $("#order_val").attr("data-value"))
    });
    $("#order_val1").on("mouseover", function () {
        console.log("Hello", $("#order_val1").attr("data-value"))
        $("#order_val1").attr("href", "/items/?order_by=" + $("#order_val1").attr("data-value"))
    });
    $("#order_val2").on("mouseover", function () {
        console.log("Hello", $("#order_val2").attr("data-value"))
        $("#order_val2").attr("href", "/items/?order_by=" + $("#order_val2").attr("data-value"))
    });
    $("#order_val3").on("mouseover", function () {
        console.log("Hello", $("#order_val3").attr("data-value"))
        $("#order_val3").attr("href", "/items/?order_by=" + $("#order_val3").attr("data-value"))
    });

});