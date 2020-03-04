var btn=document.getElementsByClassName("btn btn-danger askbtn");
function buttonClicked() {
    console.log("Button clicked");
    var subject = document.getElementsByClassName("form-control validate subject");
    var query = document.getElementsByClassName("md-textarea form-control query");
    //btn.removeEventListener("click", buttonClicked
    var subarea = document.getElementsByClassName("sub");
    var querarea = document.getElementsByClassName("quer");
    var startelemt = "<li class=\"list-group-item\">";
    subarea[0].innerHTML += startelemt + subject[0].value + "<br>"+ "</li>";
    querarea[0].innerHTML += query[0].value;
    console.log(subject[0].value, query[0].value, subarea.innerHTML, querarea.innerHTML)
}
btn[0].addEventListener("click", buttonClicked);