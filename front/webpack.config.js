const webpack = require('webpack');
const resolve = require('path').resolve;
const config = {
    devtool: 'eval-source-map',

    entry: __dirname + '/index.jsx',
    output: {
        path: resolve('../static/react'),
        filename: 'bundle.js',
        publicPath: resolve('../static/react')
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['@babel/preset-react', '@babel/preset-env']
                },
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader?modules'
            }]
    }
};
module.exports = config;