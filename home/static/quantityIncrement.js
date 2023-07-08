function incrementButton(){
    var element = document.getElementById("quantity")
    var totalValue = element.value

    ++totalValue

    console.log(value)
    document.getElementById("quantity").value = totalValue
}