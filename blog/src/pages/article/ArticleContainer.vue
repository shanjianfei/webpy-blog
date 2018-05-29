<template>
    <div class="article-container">
        <articles v-bind:type="type"></articles>
    </div>
</template>
<script>
    import articles from "@/pages/article/children/Article"
    export default {
        data() {
            return {
                type: ''
            }
        },
        components: {
            articles,
        },
        watch: {
            '$route': function(to, from) {
                let id = to.params.id
                this.type = id
            }
        }
    }
</script>