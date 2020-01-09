<template>
  <div>
        <v-card class='mx-auto'  max-width='500' style='margin:20px;padding:20px;' shaped>
            <v-list-item>
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
</template>

<script>
export default {
    props: ['memo', 'onDelete']
}
</script>

<style>

</style>