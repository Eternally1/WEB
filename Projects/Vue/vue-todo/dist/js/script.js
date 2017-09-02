(function() {
    const store = new Vuex.Store({
        //存储状态
        state: {
            Items: [],
            count: 2
        },
        //改变状态的唯一途径
        mutations: {
            newItem: function(state) {
                state.Items.unshift({
                    "text": "",
                    "label": "normal",
                    "isEditing": true,
                    "status": "undone"
                })

            },
            //保存到本地
            saveLocal: function(state) {
                window.localStorage.setItem("todo-list", JSON.stringify(state.Items));
            },
            //加载存储在本地的
            loadLocal: function(state) {
                let todolist = window.localStorage.getItem("todo-list");
                state.Items = JSON.parse(todolist);
                //如果为null，代表没有元素
                if (!state.Items) {
                    state.Items = [];
                }
                console.log(state.Items);
            }
        }
    })



    const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    //获取当前时间以及
    //1、使用vue构造器创建一个子类
    const header = Vue.extend({
        template: "#todo-header",
        data() {
            //初始值先设定为空
            return {
                day: "",
                dayofweek: "",
                month: "",
                Items: store.state.Items
            }
        },
        // 使用mounted钩子函数，
        mounted: function() {
            //this的指向就是data
            let date = new Date();
            //返回某一天
            this.day = date.getDate();
            //返回一周中的某一天
            this.dayofweek = weekday[date.getDay()];
            //获取年月
            this.month = month[date.getMonth()] + "," + date.getFullYear();
        },
        methods: {
            add: function() {
                store.commit('newItem');
            }
        }
    });

    const title = Vue.extend({
        template: "#todo-content-title",
        data() {
            return {

            }
        },
        computed: {
            allTasks: function() {
                return store.state.Items.length
            }
        }
    });

    const list = Vue.extend({
        template: "#todo-list",
        data() {
            return {
                //临时的保存的值。用于在save的使用用。
                tempText: ""
            }
        },
        computed: {
            Items: function() {
                return store.state.Items
            }
        },
        mounted: function() {
            store.commit('loadLocal');
        },
        methods: {
            //将当前对象传递进来
            save(item) {
                //此时，如果想将内容填到Items中比较麻烦，需要对应，因此这里最好修改使用vuex管理状态
                if (this.tempText.trim() != "") {
                    item.text = this.tempText;
                    //让状态变成不可编辑
                    item.isEditing = false;
                    store.commit('saveLocal');
                }
                //每次保存之后tempText清空
                this.tempText = "";
                console.log(store.state.Items);
            },
            showAction: function(ev) {
                //阻止事件冒泡
                ev.stopPropagation();
                //获取当前选择对象
                let target = ev.currentTarget;
                let actionList = target.getElementsByClassName("action-list")[0];
                //判断是否有类show，没有的话直接添加，有的话就删除
                if (actionList.className.indexOf("show") == -1) {
                    actionList.className += " show ";
                } else if (actionList.className.indexOf("show") != -1) {
                    actionList.className = actionList.className.replace("show", "");
                }
            },
            showLable: function(ev) {
                //阻止事件冒泡
                ev.stopPropagation();
                let target = ev.currentTarget;
                let labelList = target.getElementsByClassName("label-list")[0];
                if (labelList.className.indexOf("show") == -1) {
                    labelList.className += " show ";
                } else if (labelList.className.indexOf("show") != -1) {
                    labelList.className = labelList.className.replace("show", "");
                }
            },
            //将当前任务的状态设置成已经完成，背景颜色改变并且移到数组的最后面
            makedownAct: function(item) {
                item.status = "done";
                store.commit("saveLocal");
            },
            editAct: function(item) {
                //当要编辑的时候，将之前的内容显示在input框
                this.tempText = item.text;
                item.isEditing = true;
                store.commit('saveLocal');
            },
            deleteAct: function(item) {
                console.log(JSON.stringify(store.state.Items));
                console.log(JSON.stringify(item));
                console.log(item);
            }
        }
    })

    //2、通过实例化加载到#app中
    const todo = new Vue({
        el: "#app",
        store,
        created: function() {
            window.addEventListener("click", this.hideActionList);
            window.addEventListener("click", this.hideLabelList);
        },
        methods: {
            hideActionList: function() {
                //如果actionList是显示的，当点击任意位置时可以隐藏起来。
                let action_lists = document.getElementsByClassName("action-list");
                for (let i = 0; i < action_lists.length; i++) {
                    if (action_lists[i].className.indexOf("show") != -1) {
                        action_lists[i].className = action_lists[i].className.replace("show", "");
                    }
                }
            },
            hideLabelList: function() {
                let label_lists = document.getElementsByClassName("label-list");
                for (let i = 0; i < label_lists.length; i++) {
                    if (label_lists[i].className.indexOf("show") != -1) {
                        label_lists[i].className = label_lists[i].className.replace("show", "");
                    }
                }
            }
        },
        components: {
            'todo-header': header,
            'todo-content-title': title,
            'todo-list': list
        }
    });
    Vue.directive('focus', {
        // 当绑定元素插入到 DOM 中。
        inserted: function(el) {
            // 聚焦元素
            el.focus()
        }
    });
})();