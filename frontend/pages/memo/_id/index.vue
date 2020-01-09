<template>
  <div>
      <h1> MEMO DETAILS </h1>

    <div>
          <div> {{memo.id}}</div>
          <div> {{memo.name}}</div>
          <div> {{memo.phone}}</div>
          <div> {{memo.address}}</div>
          <div>{{memo.date}}</div>
          
      </div>





  </div>
</template>

<script>
export default {
    
    head(){
        return{
            title: 'view memo'
        }
    },


    data(){
        return{
            memo: []
        }
    },


    async asyncData({$axios, params}) {
        try{
            let memo = await $axios.$get(`/memo/${params.id}`)
            console.log(memo)
            return{ memo }
        } catch(e){}s
            console.log(e)
    },









}
</script>

<style>

</style>