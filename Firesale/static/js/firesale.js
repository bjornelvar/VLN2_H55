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
});

