<template>
	<div id="app">
		<toolbar></toolbar>
		<notes-list></notes-list>
		<editor></editor>
	</div>
</template>
<script>
import ToolBar from './ToolBar.vue'
import NotesList from './NotesList.vue'
import Editor from './Editor.vue'

export default{
	components:{
		ToolBar,
		NotesList,
		Editor
	}
}

</script>