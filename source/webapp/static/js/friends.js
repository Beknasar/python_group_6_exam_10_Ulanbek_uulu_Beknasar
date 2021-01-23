async function addFriend(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;
    console.log(addBtn);
    console.log(addBtn.href);
    try {
        await makeRequest(url, 'POST');
        console.log("Добавлено в друзья");
        location.reload()
    }
    catch (error) {
        console.log(error);
    }
}

async function removeFriend(event) {
    event.preventDefault();
    let removeBtn = event.target;
    let url = removeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Удалено из друзей")
        location.reload()
    }
    catch (error) {
        console.log(error);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('addFriend');
    const removeButtons = document.getElementsByClassName('removeFriend');

    for (let btn of addButtons) {btn.onclick = addFriend}
    for (let btn of removeButtons) {btn.onclick = removeFriend}
});