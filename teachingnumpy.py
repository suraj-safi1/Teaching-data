{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "teachingnumpy.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNBg68pvwSYQBYJfG790PdC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/suraj-safi1/Teaching-data/blob/main/teachingnumpy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tSWvFu5lJGDZ",
        "outputId": "290ebfec-768b-4dde-cf26-8351867c3ce6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (1.1.5)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas) (2018.9)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: numpy>=1.15.4 in /usr/local/lib/python3.7/dist-packages (from pandas) (1.19.5)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n"
          ]
        }
      ],
      "source": [
        "pip install pandas\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install numpy\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SckzNAaWJPss",
        "outputId": "c8e19177-cab5-4b5e-fb0e-df2a6161e7f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (1.19.5)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "height=np.array([100,123,234,79,109])"
      ],
      "metadata": {
        "id": "KQ94AiTKJctx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type (height)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tBSOwmDaMK8Y",
        "outputId": "bdd92a8a-51fc-4ac7-9c20-408b15033277"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "numpy.ndarray"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "height[2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CQ3hSlVJMQKy",
        "outputId": "e36ec87f-e154-4100-c302-9a156254e883"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "79.0"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(height[0:3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iWqe1hdIMhLQ",
        "outputId": "6cbd57f3-9357-42a6-a865-cee7db45949c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[100 123 234]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=np.ones([3,4])\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "buy6p5kKNDX7",
        "outputId": "5b268571-e838-4233-91c1-19d9f2c0d2f6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1. 1. 1. 1.]\n",
            " [1. 1. 1. 1.]\n",
            " [1. 1. 1. 1.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.mean(height)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6xxTvUbwNsdK",
        "outputId": "f7f2c732-7340-4911-b590-026167e585c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "129.0"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sum(height)/len(height)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yte0AslSNwyq",
        "outputId": "ff484475-ab4a-45d9-d313-0e7d3d7472ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "129.0"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    }
  ]
}