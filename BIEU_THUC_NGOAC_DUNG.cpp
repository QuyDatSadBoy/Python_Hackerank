#include <bits/stdc++.h>
#pragma gcc optimize("Ofast")
#define endl '\n'
using namespace std;

using ll = long long;

char p[8] = {'(', ')', '[', ']', '{', '}', '<', '>'};

string s;
ll cnt = 0;

bool checkres(string s)
{
	stack<char> st;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '(' || s[i] == '{' || s[i] == '[' || s[i] == '<')
		{
			st.push(s[i]);
		}
		else
		{
			if (!st.empty())
			{
				char x = st.top();
				if ((x == '(' && s[i] == ')') || (x == '[' && s[i] == ']') || (x == '<' && s[i] == '>') || (x == '{' && s[i] == '}'))
				{
					st.pop();
				}
				else
					return false;
			}
			else
				return false;
		}
	}
	return st.empty();
}

bool check1(string s)
{
	stack<char> st;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '(' || s[i] == '{' || s[i] == '[' || s[i] == '<')
		{
			st.push(s[i]);
		}
		else
		{
			if (!st.empty())
			{
				char x = st.top();
				if ((x == '(' && s[i] == ')') || (x == '[' && s[i] == ']') || (x == '<' && s[i] == '>') || (x == '{' && s[i] == '}'))
				{
					st.pop();
				}
				else
					return false;
			}
			else
				return false;
		}
	}
	return true;
}
void Try(int i)
{
	if (i == s.size() - 1)
	{
		if (checkres(s))
			cnt++;
	}
	if (s[i] == '?')
	{
		for (int j = 0; j < 8; j++)
		{
			s[i] = p[j];
			string substr = "";
			for (int k = 0; k <= i; k++)
			{
				substr += s[k];
			}
			if (check1(substr))
			{
				Try(i + 1);
			}
			s[i] = '?';
		}
	}
	else if (i < s.size() - 1)
		Try(i + 1);
}

int main()
{
	ll t;
	cin >> t;
	cin.ignore(1);
	while (t--)
	{
		cin >> s;
		Try(0);
		cout << cnt << endl;
		cnt = 0;
	}
	return 0;
}

/* (??)       5
   (<{}>??]   1
   (?]]       0
*/
