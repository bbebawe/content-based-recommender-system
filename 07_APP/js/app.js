let query = $("#search-box").val();

var app = new Vue({
    el: "#app",
    data: {
        searchKeyword: query,
        loading: false,
        validTitle: true,
        movies: {}
    },
    methods: {
        getRecommendations: function() {
            if (app.validTitle == true && app.searchKeyword.length > 3) {
                app.loading = true;
                $(".fullHeader").animate(
                    {
                        minHeight: "3vh"
                    },
                    1000
                );
                $(".content").animate(
                    {
                        paddingTop: "2%",
                        paddingBottom: "30px"
                    },
                    1000
                );
                $("header").css({ position: "fixed" });
                $("main").css({ opacity: ".5" });
                fetch(
                    `http://127.0.0.1:5000/api/getRecs?movie=${app.searchKeyword}`
                )
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        app.loading = false;
                        app.movies = data;
                        console.log(data);
                        $("main").css({ opacity: "1" });
                        $("#recommendations").css({ display: "block" });
                    });
            }
        }
    }
});

$("#search-box").autocomplete({
    source: function(request, response) {
        $.getJSON(
            "http://127.0.0.1:5000/api/autocomplete",
            {
                query: request.term // in flask, "q" will be the argument to look for using request.args
            },
            function(data) {
                if (data.length > 0) {
                    app.validTitle = true;
                    response(data); // matching_results from jsonify
                } else {
                    response([]);
                    app.validTitle = false;
                }
            }
        );
    },
    minLength: 3,
    delay: 500,
    select: function(event, ui) {
        // console.log(ui.item.value); // not in your question, but might help later
        $("#search-box").val(ui.item.label);
        app.searchKeyword = ui.item.label;
        console.log("the value is " + ui.item.label);
    }
});
