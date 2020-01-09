<template>
  <div>

        <span>MEMO LIST | </span> <v-btn nuxt to='memo/add'>add</v-btn>


        <div style='margin:20px;'>
         <v-card class='mx-auto'  max-width='500' style='margin:20px;padding:20px;' shaped v-for="memo in memoData" v-bind:key="memo.id"> 
            <v-list-item  >
                    <v-list-item-content>
                            <div class='overline mb-4'>{{memo.date}}</div>
                            <v-list-item-title class='headline mb-5'>{{memo.name}}</v-list-item-title>
                            <v-list-item-subtitle>{{memo.phone}}</v-list-item-subtitle>
                            <v-list-item-subtitle>{{memo.address}}</v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-avatar tile size='80' color='grey'> </v-list-item-avatar>
            </v-list-item>

            <v-card-actions >
                <v-btn text> UPDATE </v-btn>
                <v-btn text @click='onDelete(memo.id)'> DELETE </v-btn>
            </v-card-actions>
        </v-card>
        </div>


  </div>
</template>

<script>


export default {

    components: {
      
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