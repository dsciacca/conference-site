var errorMessage = "";
var votes = [0, 0, 0];


window.onload=function(){
    var location = window.location.href;
    if(location.indexOf('registration.html') >= 0 ){
        console.log('here1');
        var regSubmitBtn = document.getElementById('registration');
        regSubmitBtn.addEventListener('click', function(){
            makeRegCookie();
            verifyRegistration();
        }, false);
        var cookieEl = document.getElementById('idNum');
        cookieEl.addEventListener('blur', function(){getRegCookie('123456')}, false);
    } else if (location.indexOf('poll.html') >= 0){
        if(localStorage.getItem("votes") == null){
            localStorage.setItem("votes", votes);
        }
        console.log(localStorage.getItem("votes"));
        var pollSubmitBtn = document.getElementById('pollsubmit');
        if(pollSubmitBtn != null){
            pollSubmitBtn.addEventListener('click', function(){
                makeVoteCookie();
                displayThankYou();
            }, false);
            getVotesCookie('votes');
        }
    }
}

function displayThankYou(){
    var name;
    if (document.getElementById('janedoe').checked){
        name = 'Jane Doe';
    } else if (document.getElementById('joeshmoe').checked){
        name = 'Joe Shmoe';
    } else if (document.getElementById('rondarae').checked){
        name = 'Ronda Rae';
    }
    alert('Thanks for voting for: ' + name);
}


function verifyRegistration(){
    if ((document.getElementById('exl').checked && document.getElementById('email').checked) ||
        (document.getElementById('exl').checked && document.getElementById('one-on-one').checked) ||
        (document.getElementById('exl').checked && document.getElementById('presentation').checked)){
        errorMessage = "Because you registered for the excel workshop, you cannot register for any workshops in " +
            "session 2, please go back and re-register";
        localStorage.setItem("Error Message", errorMessage);
        displayError();
    } else if (!document.getElementById('exl').checked && !document.getElementById('email').checked &&
        !document.getElementById('one-on-one').checked && !document.getElementById('presentation').checked){
        errorMessage = "Since you did not choose the excel workshop in session 1, you must select a workshop in " +
            "session 2, please go back and re-register";
        localStorage.setItem("Error Message", errorMessage);
        displayError();
    } else if ((document.getElementById('presentation').checked && !document.getElementById('focus').checked) ||
        (document.getElementById('focus').checked && !document.getElementById('presentation').checked)){
        errorMessage = "If you want to take either the Presentation Etiquette or the Focus Strategies workshop, you " +
            "must also take the other, please go back and re-register";
        localStorage.setItem("Error Message", errorMessage);
        displayError();
    } else if (document.getElementById('exl').checked && document.getElementById('focus').checked){
        errorMessage = "You cannot take the Excel workshop with the Focus Strategies workshop because you must take " +
            "Presentation Etiquette with Focus Strategies, but the Excel workshop takes up session 2 as well, please " +
            "go back and re-register";
        localStorage.setItem("Error Message", errorMessage);
        displayError();
    } else {
        console.log('sending to thankyou.html');
        window.location.href="../../templates/thankyou.html";
    }
}

function displayError(){
    var centerLeft = parseInt((window.screen.availWidth - 500) / 2);
    var centerTop = parseInt((window.screen.availHeight - 400) / 2);
    var newWindow = window.open('error.html', 'invalid entry', 'width=500px,height=400px,left=' + centerLeft + ',top='
        + centerTop + ',location=0');
    newWindow.status = "An Invalid Entry Occurred During Registration";
}

function displayMsg(msg){
    document.getElementById("error").innerHTML = msg;
}

function closeWindow(){
    window.close();
}

function onLoad(){
    displayMsg(localStorage.getItem("Error Message"));
}

function makeRegCookie(){
    var idNum = document.getElementById('idNum').value;
    var title = document.getElementById('title').value;
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var address1 = document.getElementById('address1').value;
    var address2  = document.getElementById('address2').value;
    var city = document.getElementById('city').value;
    var state = document.getElementById('state').value;
    var zip = document.getElementById('zip').value;
    var telNum = document.getElementById('telNum').value;
    var emailAddress = document.getElementById('emailAddress').value;
    var website = document.getElementById('website').value;
    var companyPos = document.getElementById('companyPos').value;
    var companyName = document.getElementById('companyName').value;
    var mealPlan;
    if(document.getElementById('fullMeal').checked){
        mealPlan = 'fullMeal';
    } else if (document.getElementById('dinnerOnly').checked){
        mealPlan = 'dinnerOnly';
    }
    var billFirstName = document.getElementById('billFirstName').value;
    var billLastName = document.getElementById('billLastName').value;
    var cardType;
    if(document.getElementById('visa').checked){
        cardType = 'visa';
    }else if(document.getElementById('amx').checked){
        cardType = 'amx';
    }else if(document.getElementById('master').checked){
        cardType = 'master';
    }
    var cardNum = document.getElementById('cardNum').value;
    var csv = document.getElementById('csv').value;
    var expYr = document.getElementById('expYr').value;
    var expMnth = document.getElementById('expMnth').value;
    var workshop1;
    if(document.getElementById('ppt').checked){
        workshop1 = 'ppt';
    } else if (document.getElementById('exl').checked){
        workshop1 = 'exl';
    } else if (document.getElementById('word').checked){
        workshop1 = 'word';
    }
    var workshop2;
    if(document.getElementById('email').checked){
        workshop2 = 'email';
    } else if (document.getElementById('one-on-one').checked){
        workshop2 = 'one-on-one';
    } else if (document.getElementById('presentation').checked){
        workshop2 = 'presentation';
    }
    var workshop3;
    if(document.getElementById('team').checked){
        workshop3 = 'team';
    } else if (document.getElementById('focus').checked){
        workshop3 = 'focus';
    } else if (document.getElementById('com').checked){
        workshop3 = 'com';
    }
    document.cookie = idNum + "=" + "title:" + title + "#firstname:" + firstName + "#lastname:" + lastName
        + "#address1:" + address1 + "#address2:" + address2 + "#city:" + city + "#state:" + state + "#zip:" + zip
        + "#telNum:" + telNum + "#email:" + emailAddress + "#website:" + website + "#companypos:" + companyPos
        + "#companyname:" + companyName + "#mealplan:" + mealPlan + "#billfirst:" + billFirstName + "#billlast:"
        + billLastName + "#cardtype:" + cardType + "#cardnum:" + cardNum + "#csv:" + csv + "#expYr:" + expYr
        + "#expMnth:" + expMnth + "#workshop1:" + workshop1 + "#workshop2:" + workshop2 + "#workshop3:" + workshop3
        + "; path=/";
}

function makeVoteCookie(){
    var currVotes = localStorage.getItem("votes");
    var currVotesArray = currVotes.split(',');
    console.log(currVotesArray);
    for(var i = 0; i < currVotesArray.length; i++){
        currVotesArray[i] = parseInt(currVotesArray[i], 10);
    }
    if(document.getElementById('janedoe').checked){
        currVotesArray[0]++;
    } else if (document.getElementById('joeshmoe').checked){
        currVotesArray[1]++;
    } else if (document.getElementById('rondarae').checked){
        currVotesArray[2]++;
    }
    console.log(currVotesArray);
    document.cookie = "votes=jane:" + currVotesArray[0] + "#joe:" + currVotesArray[1] + "#ronda:" + currVotesArray[2];
    localStorage.setItem("votes", currVotesArray);
    console.log(localStorage.getItem("votes"));
}

function getRegCookie(cookieInfo){
    var name = cookieInfo + "=";
    console.log(name);
    var result = decodeURIComponent(document.cookie);
    console.log(result);
    var cookieArray = result.split(';');
    console.log(cookieArray);
    for(var i = 0; i < cookieArray.length; i++){
        var cookie = cookieArray[i];
        console.log("pass" + i +" substring=" + cookie);
        while (cookie.charAt(0) == ' '){
            cookie = cookie.substring(1);
            console.log(cookie);
        }
        var cookieData = cookie.split('=');
        if(cookieData[0] == "123456"){
            var valuesArray = cookieData[1].split('#');
            for(var j = 0; j < valuesArray.length; j++){
                console.log(valuesArray[j]);
                var currArray = valuesArray[j].split(':');
                console.log(currArray);
                var value = currArray[1];
                switch (currArray[0]){
                    case 'title':
                        console.log('right here!');
                        document.getElementById('title').value = value;
                        console.log('and breaking');
                        break;
                    case 'firstname':
                        document.getElementById('firstName').value = value;
                        break;
                    case 'lastname':
                        document.getElementById('lastName').value = value;
                        break;
                    case 'address1':
                        document.getElementById('address1').value = value;
                        break;
                    case 'address2':
                        document.getElementById('address2').value = value;
                        break;
                    case 'city':
                        document.getElementById('city').value = value;
                        break;
                    case 'state':
                        document.getElementById('state').value = value;
                        break;
                    case 'zip':
                        document.getElementById('zip').value = value;
                        break;
                    case 'telNum':
                        document.getElementById('telNum').value = value;
                        break;
                    case 'email':
                        document.getElementById('emailAddress').value = value;
                        break;
                    case 'website':
                        if(value != ""){
                            document.getElementById('website').value = value + ":" + currArray[2];
                        }
                        break;
                    case 'companypos':
                        document.getElementById('companyPos').value = value;
                        break;
                    case 'companyname':
                        document.getElementById('companyName').value = value;
                        break;
                    case 'mealplan':
                        if(value == 'fullMeal'){
                            document.getElementById('fullMeal').checked = true;
                        } else if(value == 'dinnerOnly'){
                             document.getElementById('dinnerOnly').checked = true;
                        }
                        break;
                    case 'billfirst':
                        document.getElementById('billFirstName').value = value;
                        break;
                    case 'billlast':
                        document.getElementById('billLastName').value = value;
                        break;
                    case 'cardtype':
                        if(value == 'visa'){
                            document.getElementById('visa').checked = true;
                        }else if(value == 'amx'){
                            document.getElementById('amx').checked = true;
                        }else if(value == 'master'){
                            document.getElementById('master').checked = true;
                        }
                        break;
                    case 'cardnum':
                        document.getElementById('cardNum').value = value;
                        break;
                    case 'csv':
                        document.getElementById('csv').value = value;
                        break;
                    case 'expYr':
                        document.getElementById('expYr').value = value;
                        break;
                    case 'expMnth':
                        document.getElementById('expMnth').value = value;
                        break;
                    case 'workshop1':
                        if(value == 'ppt'){
                            document.getElementById('ppt').checked = true;
                        }else if(value == 'exl'){
                            document.getElementById('exl').checked = true;
                        }else if(value == 'word'){
                            document.getElementById('word').checked = true;
                        }
                        break;
                    case 'workshop2':
                        if(value == 'email'){
                            document.getElementById('email').checked = true;
                        }else if(value == 'one-on-one'){
                            document.getElementById('one-on-one').checked = true;
                        }else if(value == 'presentation'){
                            document.getElementById('presentation').checked = true;
                        }
                        break;
                    case 'workshop3':
                        if(value == 'team'){
                            document.getElementById('team').checked = true;
                        }else if(value == 'focus'){
                            document.getElementById('focus').checked = true;
                        }else if(value == 'com'){
                            document.getElementById('com').checked = true;
                        }
                        break;
                }
            }
        }
    }
}

function getVotesCookie(cookieInfo){
    var name = cookieInfo + "=";
    console.log(name);
    var result = decodeURIComponent(document.cookie);
    console.log(result);
    var cookieArray = result.split(';');
    console.log(cookieArray);
    for(var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i];
        console.log("pass" + i + " substring=" + cookie);
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
            console.log(cookie);
        }
        var cookieData = cookie.split('=');
        var janeVotes = document.getElementById('janevotes');
        var joeVotes = document.getElementById('joevotes');
        var rondaVotes = document.getElementById('rondavotes');
        if (cookieData[0] == 'votes') {
            var valuesArray = cookieData[1].split('#');
            for (var j = 0; j < valuesArray.length; j++) {
                console.log(valuesArray[j]);
                var currArray = valuesArray[j].split(':');
                var value = currArray[1];
                switch (currArray[0]) {
                    case 'jane':
                        janeVotes.textContent = value;
                        break;
                    case 'joe':
                        joeVotes.textContent = value;
                        break;
                    case 'ronda':
                        rondaVotes.textContent = value;
                        break;
                }
            }
            break; //breaks out of loop so doesn't set to zero in else clause when on different cookie
        } else {
            janeVotes.textContent = 0;
            joeVotes.textContent = 0;
            rondaVotes.textContent = 0;
        }
    }
}

function displayWorkshopList(){
    console.log('entering displayWorkshopList()');
    var word = document.getElementById('word');
    var exl = document.getElementById('exl');
    var ppt = document.getElementById('ppt');
    var email = document.getElementById('email');
    var one_on_one = document.getElementById('one_on_one');
    var presentation = document.getElementById('presentation');
    var team = document.getElementById('team');
    var focus = document.getElementById('focus');
    var com = document.getElementById('com');
    if(word.checked){
        window.open('participantlists/Workshop1.html');
    }
    if(exl.checked){
        window.open('participantlists/Workshop2.html');
    }
    if(ppt.checked){
        window.open('participantlists/Workshop3.html');
    }
    if(email.checked){
        window.open('participantlists/Workshop4.html');
    }
    if(one_on_one.checked){
        window.open('participantlists/Workshop5.html');
    }
    if(presentation.checked){
        window.open('participantlists/Workshop6.html');
    }
    if(team.checked){
        window.open('participantlists/Workshop7.html');
    }
    if(focus.checked){
        window.open('participantlists/Workshop8.html');
    }
    if(com.checked){
        window.open('participantlists/Workshop9.html');
    }
}

function displayMealList(){
    var full = document.getElementById('full');
    var dinner = document.getElementById('dinner');
    if(full.checked){
        window.open('participantlists/mealpack.html');
    }
    if(dinner.checked){
        window.open('participantlists/dinnerday2.html');
    }
}
