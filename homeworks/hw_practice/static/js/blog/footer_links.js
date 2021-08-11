$(document).ready(function () {
    $.ajax({
        method: "GET",
        url: "/api/footer-useful-links",
        success: function (data) {
            if (data.success) {
                for (let el of data.items) {
                    let footerLinkHtml = "<p>" + "<a href=\"" + el.link + "\">" + el.name + "</a></p>"
                    $("#footerLinksList").append(footerLinkHtml);
                }
            }
        }
    });
});
