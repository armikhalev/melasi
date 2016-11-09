$(document).ready(function(){

  $('#json').click(function(){
       $.getJSON("http://localhost/koyla/english/wife",
       function(data) {
          $("#test").html(data[0].word);
          console.log(data[0]);
        });
  });

  $('#ajax').click(function(){
       $.ajax({
           type: "GET",
           dataType: "json",
           url: "http://localhost/koyla/english/wife",
           success: function(data){
              $("#test").html(data[0].la);
              console.log(data[0]);
           }
       });
  });

});
