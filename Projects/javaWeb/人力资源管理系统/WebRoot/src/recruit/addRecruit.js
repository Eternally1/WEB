function $getId(id) {
    return document.getElementById(id);
}
/**
 * 保存事件
 */
let save = $getId("save"),
    reset = $getId("reset"),
    name = $getId("name"),
    age = $getId("age"),
    job = $getId("job"),
    specialty = $getId("specialty"),
    experience = $getId("experience"),
    school = $getId("school"),
    tel = $getId("tel"),
    email = $getId("email"),
    content = $getId("content");

reset.onclick = function(){
	name.value = "";
	age.value = "";
	job.value="";
	specialty.value = "";
	experience.value = "";
	school.value = "";
	tel.value ="";
	email.value = "";
	content.value = "";
}

save.onclick = function() {
    if(!checkIsEmpty()){
        return;
    }
    let data = {
        name: name.value.trim(),
        sex: checkRadio("sex"),
        age: age.value.trim(),
        job: checkSelect("job"),
        specialty: specialty.value.trim(),
        experience: experience.value.trim(),
        studyeffort: checkSelect("studyeffort"),
        school: school.value.trim(),
        tel: tel.value.trim(),
        email: email.value.trim(),
        content: content.value.trim()
    };
    myApi.recruit.addRecruit(data, function(err, res) {
        if (err) {
            alert(err);
        } else {
            alert(res);
            location.href = "./showRecruit.html"
        }
    });
}

function checkIsEmpty(){
    let telReg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
    let emailReg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
    if (!name.value.trim()) {
        name.focus();
        alert("请填写用户名");
        return false;
    }else if (!telReg.test(tel.value)){
        tel.focus();
        alert("请填写正确的手机号");
        return false;
    }else if(!emailReg.test(email.value)){
        alert("请输入正确的email");
        email.focus();
        return false
    }
    return true;
}

function checkRadio(radioname) {
    let rLists = document.getElementsByName(radioname),
        radioV,
        i;
    for (i = 0; i < rLists.length; i++) {
        if (rLists[i].checked) {
            radioV = rLists[i].value;
            return radioV;
        }
    }
}

function checkSelect(selectid) {
    let select = document.getElementById(selectid);
    //选中的索引
    let index = select.selectedIndex;
    //选中的值
    // console.log(select.options[index].value);
    //选中的文本
    // console.log(select.options[index].text);
    return select.options[index].value;
}