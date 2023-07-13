let firstButton = document.getElementById('SearchUser')
let secondButton = document.getElementById('reqUser')

firstButton.onclick = function (){
    BX24.selectUser(function (res){
        secondButton.disabled = false;
        secondButton.style.background = '#4CAF50';
        secondButton.style.cursor = 'pointer';
        secondButton.value = res['id'];
    })
}
