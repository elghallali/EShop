
$('.plus-cart').click(function () {
    //console.log('button clicked');
    //console.log(this.parentNode);
    let id = $(this).attr("pid").toString()
    let elm = this.parentNode.children[2]
    console.log('pid = ', id)
    $.ajax({
        type: "GET",
        url: "/plus-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            elm.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total_amount
        }
    })

})

$('.minus-cart').click(function () {
    //console.log('button clicked');
    //console.log(this.parentNode);
    let id = $(this).attr("pid").toString()
    let elm = this.parentNode.children[2]
    console.log('pid = ', id)
    $.ajax({
        type: "GET",
        url: "/minus-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            elm.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total_amount
        }
    })

})

$('.remove-cart').click(function () {
    //console.log('button clicked');
    //console.log(this.parentNode);
    let id = $(this).attr("pid").toString()
    let elm = this
    $.ajax({
        type: "GET",
        url: "/remove-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total_amount
            elm.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })

})