chrome.runtime.sendMessage({ todo: "showPageAction" })

window.addEventListener('DOMFocusIn', function () {

    let stars = [];

    document.querySelector('._2teBVu').childNodes.forEach(child => stars.push(child));

    stars.reverse();
    stars.unshift(0);

    let review = document.querySelector('textarea._3kRe7w');

    review.addEventListener('keyup', function (e) {

        if (e.target.value == 'awesome') updateRating(5);
        if (e.target.value == 'decent') updateRating(3);
        if (e.target.value == 'worst') updateRating(1);
        if (e.target.value == 'great') updateRating(4);
        if (e.target.value == 'cool') updateRating(4);
        if (e.target.value == 'good') updateRating(3);
        if (e.target.value == 'bad') updateRating(1);

    });

    function updateRating(digit) {
        stars[digit].click();
    }


    // for fun
    // let body = document.querySelector('body');
    // let jokes = [
    //     "Sorry, Google is down today!",
    //     "<a href='https://duckduckgo.com'>DuckDuckGo</a> is better.",
    //     "I'm Watching You... 😶",
    //     "I know you better than you know yourself. I'm google bro.",
    //     "I'm Sick. I've overdosed on privacy",
    //     "<a href='https://duckduckgo.com'>DuckDuckGo</a> is better.",
    //     "I've been admitted in a hospital. I've overdosed on monopoly.",
    //     "<span style='color:red'>Google Virus found!!</span>",
    //     "I'm tired.",
    //     "😴"
    // ]

    // body.innerHTML = `<p>${ jokes[Math.floor(Math.random() * jokes.length)] }</p>`;


}, false);



