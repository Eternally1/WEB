import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import SignIn from '@/components/SignIn'
import Information from '@/components/Infor'
import Todolist from '@/components/todolist'
import Search from '@/components/InstantSearch'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Hello',
    //   component: Hello
    // }
      {
        path:'/signin',
        name:'SignIn',
        component:SignIn
      },
      {
        path:'/infor',
        name:'infor',
        component:Information
      },
      {
        path:'/todolist',
        name:'todolist',
        component:Todolist
      },
      {
        path:'/search',
        name:'Search',
        component:Search
      }
  ]
})
