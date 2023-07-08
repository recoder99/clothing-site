function incrementButton(){
    var element = document.getElementById("quantity")
    var totalValue = element.value

    ++totalValue

   element.value = totalValue
}

function decrementButton(){
    var element = document.getElementById("quantity")
    var totalValue = element.value

    --totalValue
    if(totalValue < 1){
        totalValue = 1
    }

   element.value = totalValue
}