//引用模板
import Point from '../components/point.vue';
import Ceshi from '../components/ceshi.vue';

//引入子路由----1
import Frame from '../frame/subroute.vue';
//引入子页面模板----2
import userIndex from '../components/user/index.vue';
import userInfo from '../components/user/info.vue';
import userLove from '../components/user/love.vue';

//配置路由
export default[
	{
		path:'/point',
		component:Point
	},
    {
        path:'/ceshi',
        component:Ceshi
    },
    //配置子路由
    {
    	path:'/user',
    	component:Frame,
    	children:[
    	{
    		path:'/',
    		component:userIndex
    	},{
    		//注意这里的写法没有加上/  /info是错误的写法，不能得到预期结果
    		path:'info',
    		component:userInfo
    	},{
    		path:'love',
    		component:userLove
    	}]
    },
    {
        path:'/*',
        component:Point
    }
]