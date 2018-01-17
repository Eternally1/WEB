import Vue from 'vue';
import Router from 'vue-router';
import layouts from '../components/layouts';

Vue.use(Router);

export default new Router({
    routes: [{
        path: '/',
        component: layouts,
        name:'Layouts'    //路径名
    }]
})