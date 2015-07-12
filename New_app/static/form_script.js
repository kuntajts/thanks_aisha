var allForms = $(".Backgroundform")
var total = allForms.length
var white = Math.round(total * .50)
var asian = Math.round(total * .32)
var black = Math.round(total * .10)
var hispanic = Math.round(total * .04)
var nameric = Math.round(total * .02)
var pameric = Math.round(total * .02)

for(var i = 0; i < allForms.length; i++) {
  var alreadyChecked = true
  var el = 0
  while (alreadyChecked){
    alreadyChecked = false
    el = Math.floor(Math.random() * allForms.length)
    for (var j = 0; j < 6; j++) {
      var inp = $(allForms[el]).find("input")
      if ($($(allForms[el]).find("input")[j]).is(":checked")) {
        alreadyChecked = true
      }
    }
  }
  if (white > 0) {
    $(allForms[el]).find("input[value='WHI']").click()
    white--
  } else if (asian > 0) {
    $(allForms[el]).find("input[value='ASIN']").click()
    asian--
  } else if (black > 0) {
    $(allForms[el]).find("input[value='BAA']").click()
    black--
  } else if (pameric > 0) {
    $(allForms[el]).find("input[value='AIAN']").click()
    pameric--
  } else if (nameric > 0) {
    $(allForms[el]).find("input[value='NHOPI']").click()
    nameric--
  } else if (hispanic > 0) {
    $(allForms[el]).find("input[value='HL']").click()
    hispanic--
  }
}