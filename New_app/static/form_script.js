var allForms = $(".Backgroundform")
total = allForms.length
white = Math.round(total * .59)
asian = Math.round(total * .35)
black = Math.round(total * .01)
hispanic = Math.round(total * .02)
nameric = Math.round(total * .01)
pameric = Math.round(total * .01)

for(var i = 0; i < allForms.length; i++) {
  if (white >= 0) {
    $(allForms[i]).find("input[value='WHI']").click()
    white--
  } else if (asian >= 0) {
    $(allForms[i]).find("input[value='ASIN']").click()
    asian--
  } else if (black >= 0) {
    $(allForms[i]).find("input[value='BAA']").click()
    black--
  } else if (pameric >= 0) {
    $(allForms[i]).find("input[value='AIAN']").click()
    pameric--
  } else {
    $(allForms[i]).find("input[value='NHOPI']").click()
    nameric--
  }

  if (hispanic >= 0) {
    $(allForms[i]).find("input[value='HL']").click()
    hispanic--
  } else {
    $(allForms[i]).find("input[value='NHL']").click()
  }
}