$("select#order_no").on("change",function(){
    var order_no_v = $('select#order_no').val();
    alert("select")
    $.ajax({
    url: "/hosts/abc/", 
    data: {
        order_no : order_no_v,
    }, 
    type: "GET",
    dataType : "json", 
    
       
 })
}); 

