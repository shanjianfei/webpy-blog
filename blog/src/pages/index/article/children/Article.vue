<template>
    <div class="article">
        <div v-for="item in infoFilter">
            <a href="#/home/articlecontent" target="_blank">
                <div class="row"><span class="label label-primary">{{item.article_type}}</span></div>
                <div class="row">
                    <div class="col-md-8 col-sm-8 col-xs-8">
                        <h2>{{item.title}}</h2>
                        <div class="detail">
                            <span>{{item.create_time}}</span>
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            <span>阅读量: {{item.clickRate}}</span>
                        </div>
                    </div>
                    <div class="col-md-4 col-sm-4 col-xs-4">
                        <img v-bind:src="'/static/img/' + item.type + '.jpg'">
                    </div>
                </div>
            </a>
        </div>
    </div>
</template>
<script>
    import {mapState, mapMutations} from 'vuex'
    export default {
        data() {
            return {
                infoFilter: [],
            }
        },
        methods: {
            ...mapMutations([
                'update'
            ]),
            filter: function() {
                // console.log(this.info)
                this.$axios.get('/article')
                .then((response) => {
                    if(response.status === 200 && response.data.status === 'success') {
                        // this.update(response.data.data);
                        this.$store.commit('update', response.data.data)
                        let id = this.$route.params.id
                        if(id === 'homepage') {
                            this.infoFilter = this.info
                        } else {
                            this.infoFilter = this.info.filter(function(element) {
                                return ((element.type + 'page') === id)
                            })
                        }
                    }
                    console.log(this.$store.state.info)
                    console.log(this.info)
                })
            }
        },
        computed: {
            getInfo() {
                return this.$store.state.info
            }
        },
        watch: {
            '$route': function(to, from) {
                let id = this.$route.params.id
                if(id === 'homepage') {
                    this.infoFilter = this.getInfo;
                } else {
                    this.infoFilter = this.getInfo.filter(function(element) {
                        return ((element.type + 'page') === id)
                    })
                }
            }
        },
        mounted: function() {
            this.$axios.get('/article')
            .then((response) => {
                if(response.status === 200 && response.data.status === 'success') {
                    this.$store.commit('update', response.data.data)
                }
            })
        },
    }
</script>
<style>
    .article {
        margin: 10px;
    }
    .article .row {
        margin-left: 0;
        margin-right: 0;
        text-align: left;
    }
    .article .detail {
        margin-top: 20px;
    }
    .article a {
        cursor: pointer;
    }
    .article>div {
        background: #2d2d2d;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .article img {
        width: 200px;
        height: 100px;
        margin-bottom: 20px;
    }
</style>