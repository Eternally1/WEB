import Vue from "vue";
import Vuex from "vuex"
Vue.use(Vuex);

const state = {
	// 笔记列表
	notes:[],
	//当前笔记
	activeNote:{}
}

const mutations = {
	// 添加笔记
	// 首先需要新建一个笔记对象，然后添加到notes数组中
	ADD_NOTE(state){
		const newNote = {
			text:"New Note",
			favorite:false
		}
		state.notes.push(newNote)
		state.activeNote = newNote;
	},
	// 编辑笔记
	// 需要使用笔记的内容text作为参数
	EDIT_NOTE(state,text){
		state.activeNote.text = text;
	},
	// 删除笔记
	DELETE_NOTE(state){
		state.notes.$remove(state.activeNote);
		state.activeNote = state.notes[0];
	},
	//favorite 
	TOGGLE_FAVORITE(state){
		state.activeNote.favorite = !state.activeNote.favorite;
	},
	//设置为当前笔记
	SET_ACTIVE_NOTE(state,note){
		state.activeNote = note;
	}
}

const store = new Vuex.Store({
	state,
	mutations
})
export default store;