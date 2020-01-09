<template>
          <v-card class='mx-auto'  max-width='500' style='margin:20px;padding:20px;' shaped>
          <v-form v-model='value' @submit.prevent='submitForm'>

            <v-list-item>
                    <v-list-item-content>
                          
                            <v-list-item-title class='headline mb-5'>
                                <v-text-field v-model='memoPost.name' :rules='nameRules' label='name'></v-text-field>
                                </v-list-item-title>
                            <v-list-item-subtitle>
                                <v-text-field v-model='memoPost.phone' :rules='nameRules' label='phone'></v-text-field>

                            </v-list-item-subtitle>
                            <v-list-item-subtitle>
                                   <v-text-field v-model='memoPost.address' :rules='nameRules' label='address'></v-text-field>
                            </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-avatar tile size='80' color='grey'> </v-list-item-avatar>
            </v-list-item>

            <v-card-actions >
                <v-btn text type='submit'> SUBMIT </v-btn>
            </v-card-actions>
        </v-form>
        </v-card>

</template>

<script>
export default {
    data(){
        return{
            value: false,
            nameRules: [
                    v => !! v || 'Any contents is required'
                ],
            memoPost: {
                name: '',
                phone: '',
                address: '',
            }
        }
    },


    async asyncData({$axios, params}){
        try{
            let memoPost = await $axios.$get(`/memo/${params.id}/`)
            return { memoPost }

        } catch(e){console.log(e)}



    },


    methods: {
        async submitForm(){

            let editMemo = this.memoPost

            const config = {
                headers: {'content-type': 'multipart/form-data'}
            }
            let formData = new FormData()
            for(let data in editMemo){
                formData.append(data, editMemo[data])
            }
            try{
                let response = await this.$axios.$patch(`/memo/${editMemo.id}/`, formData, config)
                this.$router.push('/')
            } catch(e){ console.log(e)}
        }
    }
}
</script>

<style>

</style>