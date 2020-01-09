<template>
  <div>

        <span>MEMO LIST | </span> <v-btn nuxt to='memo/add'>add</v-btn>

        <div v-for="memo in memoData" :key="memo.id">
            <memo-list :memo="memo" :onDelete='onDelete'></memo-list>
        </div>

        

  </div>
</template>

<script>

import MemoList from '../../components/MemoList.vue'
export default {
    
    components: {
      MemoList,
    },

    data(){
        return{
            memoData: []
        }
    },

    async asyncData({$axios, params}){
        try{
            let memoData = await $axios.$get(`/memo/`)
            return { memoData } 
        } catch(e){
            console.log(e)
        }
    },

    methods: {
    async onDelete(id) {
      try {
        await this.$axios.$delete(`/memo/${id}/`); // delete recipe
        let data = await this.$axios.$get("/memo/"); // get new list of recipes
        this.memoData = data; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  }
    










}
</script>

<style>

</style>