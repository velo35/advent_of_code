#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

#include <glpk.h>

using namespace std;

using blueprint = vector<int>;

int solve(const vector<int>& costs, int time)
{
    vector<int> ai(1);
    vector<int> aj(1);
    vector<double> ar(1);

    glp_prob* lp = glp_create_prob();
    glp_set_obj_dir(lp, GLP_MAX);
    
    glp_add_cols(lp, 4 * time);
    for (int i = 1; i <= 4 * time; i++) {
        glp_set_col_kind(lp, i, GLP_IV);
        glp_set_col_bnds(lp, i, GLP_LO, 0, 0);
    }

    for (int i = 0; i < time; i++) {
        glp_set_obj_coef(lp, 4 * i + 4, 1);
    }

    // initial conditions
    glp_set_col_bnds(lp, 1, GLP_FX, 1, 1);
    glp_set_col_bnds(lp, 2, GLP_FX, 0, 0);
    glp_set_col_bnds(lp, 3, GLP_FX, 0, 0);
    glp_set_col_bnds(lp, 4, GLP_FX, 0, 0);

    int row = 1;
    // max one robot per step
    glp_add_rows(lp, time - 1);
    for  (int i = 1; i < time; i++, row++) {
        glp_set_row_bnds(lp, row, GLP_UP, 0, 1);
        
        for (int j = 1; j <= 4; j++) {
            ai.push_back(row);
            aj.push_back(4 * (i - 1) + j);
            ar.push_back(-1);
            
            ai.push_back(row);
            aj.push_back(4 * i + j);
            ar.push_back(1);
        }
    }

    // robot counts cannot decrease
    glp_add_rows(lp, 4 * (time - 1));
    for (int i = 1; i < time; i++) {
        for (int j = 1; j <= 4; j++, row++) {
            glp_set_row_bnds(lp, row, GLP_LO, 0, 0);
            
            ai.push_back(row);
            aj.push_back(4 * (i - 1) + j);
            ar.push_back(-1);

            ai.push_back(row);
            aj.push_back(4 * i + j);
            ar.push_back(1);
        }
    }

    // ore
    glp_add_rows(lp, time - 1);
    for (int i = 1; i < time; i++, row++) {
        glp_set_row_bnds(lp, row, GLP_LO, -costs[0], 0);

        // ore robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 1);
        ar.push_back(-costs[0]);

        // clay robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 2);
        ar.push_back(-costs[1]);

        // obsidian robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 3);
        ar.push_back(-costs[2]);

        // geode robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 4);
        ar.push_back(-costs[4]);

        for (int j = 0; j <= i - 2; j++) {
            ai.push_back(row);
            aj.push_back(4 * j + 1);
            ar.push_back(1);
        }
    }

    // clay
    glp_add_rows(lp, time - 1);
    for (int i = 1; i < time; i++, row++) {
        glp_set_row_bnds(lp, row, GLP_LO, 0, 0);

        // obsidian robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 3);
        ar.push_back(-costs[3]);

        for (int j = 0; j <= i - 2; j++) {
            ai.push_back(row);
            aj.push_back(4 * j + 2);
            ar.push_back(1);
        }
    }

    // obsidian
    glp_add_rows(lp, time - 1);
    for (int i = 1; i < time; i++, row++) {
        glp_set_row_bnds(lp, row, GLP_LO, 0, 0);

        // geode robot cost
        ai.push_back(row);
        aj.push_back(4 * i + 4);
        ar.push_back(-costs[5]);

        for (int j = 0; j <= i - 2; j++) {
            ai.push_back(row);
            aj.push_back(4 * j + 3);
            ar.push_back(1);
        }
    }

    glp_load_matrix(lp, static_cast<int>(ai.size() - 1), ai.data(), aj.data(), ar.data());

    glp_iocp param;
    glp_init_iocp(&param);
    param.presolve = GLP_ON;
    param.msg_lev = GLP_MSG_OFF;
    glp_intopt(lp, &param);

    int obj_val = glp_mip_obj_val(lp);
    glp_delete_prob(lp);

    return obj_val;
}

int task_1(const vector<blueprint>& blueprints)
{
    int quality_levels = 0;
    for (size_t i = 0; i < blueprints.size(); i++) {
        quality_levels += (i+1) * solve(blueprints[i], 24);
    }
    
    return quality_levels;
}

int task_2(const vector<blueprint>& blueprints)
{
    int result = 1;
    for (size_t i = 0; i < 3; i++) {
        result *= solve(blueprints[i], 32);
    }
    
    return result;
}

int main()
{
    bool use_sample = false;
    string input_filename = use_sample ? "sample.txt" : "real.txt";
    ifstream in(input_filename);
    
    vector<blueprint> blueprints;

    string s;
    for (int i = 1; getline(in, s); i++) {
        regex r(R"(Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.)");
        smatch m;
        regex_match(s, m, r);

        vector<int> costs;
        transform(m.begin() + 1, m.end(), back_inserter(costs), [](auto sm) { return stol(sm.str()); });
        blueprints.push_back(costs);
    }
    
    int task1 = task_1(blueprints);
    cout << "task 1: " << task1 << endl;
    int task2 = task_2(blueprints);
    cout << "task 2: " << task2 << endl;

    return 0;
}
